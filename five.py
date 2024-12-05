import re
import time
import logging
import argparse

import math
from functools import lru_cache
from pathlib import Path


class SleighSafetyManual:

    def __init__(self, raw_data):

        self.rules, self.updates = self.parse_raw(raw_data)


    def parse_raw(self, raw_data):

        halves = raw_data.split('\n\n')

        rules = halves[0].split('\n')
        rules = [tuple(map(int, x.split('|'))) for x in rules]

        updates = halves[1].split('\n')
        updates = [tuple(map(int, x.split(','))) for x in updates]

        return rules, updates


    def mid_total(self):

        total = 0

        for update in self.updates:

            if self.check_order(update):
                total += self.get_middle(update)

        return total


    def unfixed_mid_total(self):

        total = 0

        for update in self.updates:

            if not self.check_order(update):

                fixed = self.fix_order(update)
                total += self.get_middle(fixed)

        return total


    def fix_order(self, update):

        unfixed = list(update)

        for r1, r2 in self.rules:

            try:
                i1 = unfixed.index(r1)
                i2 = unfixed.index(r2)
            except ValueError:
                continue

            if i1 > i2:

                v1 = unfixed.pop(i1)
                v2 = unfixed.pop(i2)

                unfixed.insert(i2, v1)
                unfixed.insert(i1, v2)

        if not self.check_order(unfixed):
            return self.fix_order(unfixed)

        return unfixed


    def check_order(self, update):

        for r1, r2 in self.rules:

            if r1 not in update or r2 not in update:
                continue

            if update.index(r1) > update.index(r2):
                return False

        return True


    def get_middle(self, update):

        if len(update) % 2 == 0:
            return None

        mid = int(len(update) / 2)
        return update[mid]


def parse_args():

    parser = argparse.ArgumentParser(description='2024 Advent of Code, Day 5', epilog='https://adventofcode.com/2024')
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

    ssm = SleighSafetyManual(data_in)

    ##
    # Part 1
    if not conf.p2:
        start = time.time()
        t = ssm.mid_total()
        end = time.time()
        logging.info('[Part 1] Solution: %s in %s seconds', t, round(end - start, 4))

    ##
    # Part 2
    if not conf.p1 or conf.p2:
        start = time.time()
        t = ssm.unfixed_mid_total()
        end = time.time()
        logging.info('[Part 2] Solution: %s in %s seconds', t, round(end - start, 4))

