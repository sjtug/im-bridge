"""This is a sample IM platform which simulates I/O with stdin/stdout"""

import implatform.base
import msg.usertext
import threading


class SamplePlatform(implatform.base.PlatformBase):
    def __init__(self, manager, name="SamplePlatform"):
        super(SamplePlatform, self).__init__(manager)
        self._manager = manager
        self._name = name
        self._worker = None
        self._init_done = False

    def init(self):
        self._worker = threading.Thread(target=self._run)
        self._worker.start()
        self._init_done = True

    @property
    def init_done(self):
        return self._init_done

    def _run(self):
        while True:
            s = input("Input something for {}".format(self._name))
            if self._name in s:
                self._manager.add_msg(msg.usertext.UserText(self, "Screen {}".format(self._name), s))

    def send(self, msg):
        print(msg.text)

    @property
    def name(self):
        return self._name
