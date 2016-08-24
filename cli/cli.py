from manager.manager import Manager
from implatform.sample import SamplePlatform
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description="Bridge the gap between IM platforms")
    parser.add_argument('-l', '--loglevel', dest='loglevel', default=logging.INFO, help='Set log level(Default: info[20])')
    args = parser.parse_args()
    logging.basicConfig(level=int(args.loglevel))
    m = Manager()
    s1 = SamplePlatform(m, "p1")
    s2 = SamplePlatform(m, "p2")
    m.add_im(s1)
    m.add_im(s2)
    m.run()
