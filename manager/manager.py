from msg.base import MsgBase
import queue
from zenlog import log


class Manager(object):

    def __init__(self):
        self._queue = queue.Queue()
        self._ims = []

    def add_im(self, im):
        log.info("New im appended: {}".format(im))
        self._ims.append(im)

    def add_msg(self, msg):
        if issubclass(type(msg), MsgBase):
            log.debug("New message put into queue. Msg: {}; Queue Size: {}".format(msg, self._queue.qsize()))
            self._queue.put(msg, False, 3)
        else:
            log.warning("Message is not subclass of MesBase! Ignored. Msg: {}".format(msg))

    def run(self):
        for p in self._ims:
            if not p.init_done:
                log.info("Init {}...".format(p.name))
                p.init()
        while True:
            new_msg = self._queue.get()
            log.info("New message acquired. Msg: {}".format(new_msg.text))
            for im in self._ims:
                log.debug("Sending message {} to {}".format(new_msg.text, im.name))
                if new_msg.im != im:
                    im.send(new_msg) # Should not block here
            self._queue.task_done()
