from implatform.webhook import WebhookPlatform
import json


class WebhookJsonPlatform(WebhookPlatform):

    def _input_mapper(self, s):
        j = json.loads(s)
        return self._input_json_mapper(j)

    def _output_mapper(self, msg):
        j = self._output_json_mapper(msg)
        return j.dumps(j)

    def __init__(self, manager, input_port, output_url, input_json_mapper, output_json_mapper):
        super(WebhookJsonPlatform, self).__init__(manager, input_port, output_url, self._input_mapper,
                                                  self._output_mapper)
        self._input_json_mapper = input_json_mapper
        self._output_json_mapper = output_json_mapper

    @property
    def name(self):
        return "WebhookJSON_{}_{}".format(self._input_port, self._output_url)
