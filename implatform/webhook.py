from implatform.base import PlatformBase
from msg.usertext import UserText
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import requests


class WebhookListener(BaseHTTPRequestHandler):
    def __init__(self, cb, *args):
        self._cb = cb
        BaseHTTPRequestHandler.__init__(self, *args)

    def _do(self):
        s = self.rfile.read()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self._cb(s)

    def do_GET(self):
        self._do()

    def do_POST(self):
        self._do()


class WebhookPlatform(PlatformBase):
    """
    WebhookPlatform is a simple platform which listens from and sends to webhooks
    """
    def default_input_mapper(self, s):
        return UserText(self, "", s)

    def default_output_mapper(self, msg):
        return msg.text

    def __init__(self, manager, input_port, output_url, input_mapper, output_mapper):
        """
        Initiate a WebhookPlatform object
        :param manager: imbridge.manager.Manager instance
        :param input_port: the port that WebhookPlatform listens on
        :param output_url: the webhook URL which message is sent to
        :param input_mapper: function(input_string) -> message
        :param output_mapper: function(message) -> output_string
        """
        super(WebhookPlatform, self).__init__()
        self._manager = manager
        self._input_port = input_port
        self._output_url = output_url
        self._input_mapper = input_mapper
        self._output_mapper = output_mapper
        self._init_done = False
        self._thread = None

    @property
    def name(self):
        return "WebHookPlatform_input_{}_output_{}".format(self._input_port, self._output_url)

    def init(self):
        self._thread = threading.Thread(target=self._run, args=())
        self._thread.start()
        self._init_done = True

    def init_done(self):
        return self._init_done

    def _run(self):
        def cb(s):
            msg = self._input_mapper(s)
            self._manager.add_msg(msg)

        def handle(*args):
            WebhookListener(cb, *args)

        self._server = HTTPServer(('', self._input_port), handle)
        self._server.serve_forever()

    def send(self, msg):
        s = self._output_mapper(msg)
        requests.post(self._output_url, s.encode('utf-8'))