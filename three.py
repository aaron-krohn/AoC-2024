import re
import time
import logging
import argparse

import math
from functools import lru_cache
from pathlib import Path


class MemScan:

    def __init__(self, raw_data):

        self.mem = raw_data


    def uncorrupt(self):

        total = 0

        r = re.compile(r'mul\(([0-9]+),([0-9]+)\)')

        matches = r.findall(self.mem)

        logging.info('Matches: %s', len(matches))

        for m in matches:

            total += int(m[0]) * int(m[1])

        return total


    def uncorruptable(self):

        total = 0
        mul = True

        r = re.compile("mul\(([0-9]+),([0-9]+)\)|(don't\(\))|(do\(\))")

        matches = r.findall(self.mem)

        for m in matches:

            logging.debug('M: %s', m)

            for idx, cmd in enumerate(m):

                if not cmd:
                    continue

                if cmd == "don't()":
                    mul = False
                    logging.debug("DON'T: %s", mul)
                    continue

                if cmd == 'do()':
                    mul = True
                    logging.debug('DO: %s', mul)
                    continue

                if mul:
                    try:
                        x = int(m[idx])
                        y = int(m[idx+1])
                        logging.debug('%s * %s', x, y)
                        total +=  x * y
                    except Exception as exc:
                        pass

        return total


def parse_args():

    parser = argparse.ArgumentParser(description='2024 Advent of Code, Day 3', epilog='https://adventofcode.com/2024')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', default=False, help='Show debug output')
    parser.add_argument('-t', '--test', dest='test', action='store_true', default=False, help='Use test input file')
    parser.add_argument('-p1', '--part-1', dest='p1', action='store_true', default=False, help='Only run part 1')
    parser.add_argument('-p2', '--part-2', dest='p2', action='store_true', default=False, help='Only run part 2, overrides -p1')
    parser.add_argument('-l', '--log', dest='logfile', action='store', help='Filename for writing log file')

    parsed = parser.parse_args()

    return parsed


if __name__ == '__main__':

    conf = parse_args()

    loglevel = logging.DEBUG if conf.debug else logging.INFO
    logging.basicConfig(level=loglevel, format='%(asctime)s [%(levelname)s] %(message)s', filename=conf.logfile)

    fn = [Path(__file__).stem, 'input']
    if conf.test:
        fn.insert(1, 'test')
    datafile = '.'.join(fn)

    with open(datafile, 'r') as f:
        data_in = f.read().strip()

    sm = MemScan(data_in)

    ##
    # Part 1
    if not conf.p2:
        start = time.time()
        mul = sm.uncorrupt()
        end = time.time()
        logging.info('[Part 1] Solution: %s in %s seconds', mul, round(end - start, 4))

    ##
    # Part 2
    if not conf.p1 or conf.p2:
        start = time.time()
        mulable = sm.uncorruptable()
        end = time.time()
        logging.info('[Part 2] Solution: %s in %s seconds', mulable, round(end - start, 4))

