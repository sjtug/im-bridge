import time
import msg.base


class UserText(msg.base.MsgBase):
    def __init__(self, im, username, rawtext):
        self._im = im
        self._username = username
        self._raw = rawtext
        self._time = time.localtime()

    @property
    def im(self):
        return self._im

    @im.setter
    def im(self, val):
        self._im = val

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, val):
        self._time = val

    @property
    def raw_text(self):
        return self._raw

    @raw_text.setter
    def raw_text(self, val):
        self._raw = val

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        self._username = val

    @property
    def text(self):
        return "{}在{}说: {}".format(self.username, self.im.name, self.raw_text)