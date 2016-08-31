import unittest
import msg.base


def illegal_class_construct():
    class Illegal(msg.base.MsgBase):
        @property
        def text(self):
            return 'illegal'
            # other methods are missing
    return Illegal()

def legal_class_construct():
    class Legal(msg.base.MsgBase):
        @property
        def im(self):
            return 0

        @im.setter
        def im(self, val):
            pass

        @property
        def time(self):
            return 0

        @time.setter
        def time(self, val):
            pass

        @property
        def raw_text(self):
            return 0

        @raw_text.setter
        def raw_text(self, val):
            pass

        @property
        def text(self):
            return "test"
    return Legal()

class MsgBaseTest(unittest.TestCase):
    def test_illegal_msg(self):
        self.assertRaises(TypeError, illegal_class_construct)

    def test_legal_msg(self):
        try:
            legal_class_construct()
        except TypeError as err:
            self.fail(err)

if __name__ == '__main__':
    unittest.main()