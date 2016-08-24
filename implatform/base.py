import abc


class PlatformBase(abc.ABC):
    @abc.abstractmethod
    def __init__(self, manager):
        """This method will be called to init the platform.

        Don't do complex login here. You may add extra parameter to this, but keep the default one legal."""
        super(PlatformBase, self).__init__()

    @abc.abstractmethod
    def init(self):
        """This method will be called in manager.run.

        Developers should login here and block until login finishes."""
        pass

    @property
    @abc.abstractmethod
    def init_done(self):
        """Suggests whether init has finished yet.

         Only if all platforms are init_done the mainloop of manager will run."""
        pass

    @abc.abstractmethod
    def send(self, msg):
        """Send message with given msg"""
        pass

    @abc.abstractmethod
    def name(self):
        """Im implatform source name"""
        pass
