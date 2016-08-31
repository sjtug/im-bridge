import abc


class MsgBase(abc.ABC):
    @property
    @abc.abstractmethod
    def im(self):
        """Base abstract method of im getter """
        pass

    @im.setter
    @abc.abstractmethod
    def im(self, val):
        """Base abstract method of im setter"""
        pass

    @property
    @abc.abstractmethod
    def text(self):
        """Base abstract method of text getter"""
        pass

    @property
    @abc.abstractmethod
    def time(self):
        """Base abstract method of time getter"""
        pass

    @time.setter
    @abc.abstractmethod
    def time(self, val):
        """Base abstract method of time setter"""
        pass

    @property
    @abc.abstractmethod
    def raw_text(self):
        """Base abstract method of rawText getter"""
        pass

    @raw_text.setter
    @abc.abstractmethod
    def raw_text(self, val):
        """Base abstract method of rawText setter"""
        pass

    @property
    def username(self):
        return None

    @username.setter
    def username(self, val):
        raise NotImplementedError("User name is not implemented , thus can't be set")
