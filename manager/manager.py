from msg.base import MsgBase
import queue
import logging


class Manager(object):

    def __init__(self):
        self._queue = queue.Queue()
        self._ims = []

    def add_im(self, im):
        logging.info("New im appended: {}".format(im))
        self._ims.append(im)

    def add_msg(self, msg):
        if issubclass(type(msg), MsgBase):
            logging.debug("New message put into queue. Msg: {}; Queue Size: {}".format(msg, self._queue.qsize()))
            self._queue.put(msg, False, 3)
        else:
            logging.warning("Message is not subclass of MesBase! Ignored. Msg: {}".format(msg))

    def run(self):
        for p in self._ims:
            if not p.init_done:
                logging.info("Init {}...", p.name)
                p.init()
        while True:
            new_msg = self._queue.get()
            logging.info("New message acquired. Msg: {}".format(new_msg))
            for im in self._ims:
                logging.debug("Sending message {} to {}", new_msg, im)
                if new_msg.im != im:
                    im.send(new_msg) # Should not block here
            self._queue.task_done()
