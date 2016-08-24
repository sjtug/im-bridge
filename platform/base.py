import abc


class PlatformBase(abc.ABC):
    @abc.abstractmethod
    def __init__(self, manager):
        super(PlatformBase, self).__init__()

    @abc.abstractmethod
    def send(self, msg):
        """Send message with given msg"""
        pass

    @abc.abstractmethod
    def name(self):
        """Im platform source name"""
        pass