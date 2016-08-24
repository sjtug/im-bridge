import abc


class PlatformBase(abc.ABC):
    @abc.abstractmethod
    def __init__(self, manager):
        super(PlatformBase, self).__init__()

    @abc.abstractmethod
    def init(self):
        """This method will be called in manager.run"""
        pass

    @property
    @abc.abstractmethod
    def init_done(self):
        pass

    @abc.abstractmethod
    def send(self, msg):
        """Send message with given msg"""
        pass

    @abc.abstractmethod
    def name(self):
        """Im implatform source name"""
        pass
