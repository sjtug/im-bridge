from manager.manager import Manager
from implatform.sample import SamplePlatform


def main():
    m = Manager()
    s1 = SamplePlatform(m, "p1")
    s2 = SamplePlatform(m, "p2")
    m.add_im(s1)
    m.add_im(s2)
    m.run()
