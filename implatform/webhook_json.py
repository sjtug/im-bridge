from implatform.webhook import WebhookPlatform
import json


class WebhookJsonPlatform(WebhookPlatform):
    """
    WebhookJSONPlatform is a platform that listens from/sends to JSON webhooks, built on WebhookPlatform
    """
    def _input_mapper(self, s):
        j = json.loads(s)
        return self._input_json_mapper(j)

    def _output_mapper(self, msg):
        j = self._output_json_mapper(msg)
        return j.dumps(j)

    def __init__(self, manager, input_port, output_url, input_json_mapper, output_json_mapper):
        """
        Initiative a WebhookJsonPlatform object
        :param manager: im.manager.Manager instance
        :param input_port: incoming webhook port of local host that this object listens on
        :param output_url: remote URL of webhook that messages are sent to
        :param input_json_mapper: function(json) -> message
        :param output_json_mapper: function(message) -> json
        """
        super(WebhookJsonPlatform, self).__init__(manager, input_port, output_url, self._input_mapper,
                                                  self._output_mapper)
        self._input_json_mapper = input_json_mapper
        self._output_json_mapper = output_json_mapper

    @property
    def name(self):
        return "WebhookJSON_{}_{}".format(self._input_port, self._output_url)
