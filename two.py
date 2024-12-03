import time
import logging
import argparse

import math
from functools import lru_cache
from pathlib import Path


class Safety:

    def __init__(self, raw_data):

        self.data = []
        self.safety = self.parse_raw(raw_data)


    def parse_raw(self, raw_data):

        out = []

        for row in raw_data.split('\n'):

            if not row:
                continue

            row_list = list(map(int, row.split(' ')))

            self.data.append(row_list)


    def all_incr(self, row):

        if len(row) < self.min_length:
            return False

        for idx in range(len(row) - 1):

            if row[idx] >= row[idx+1]:

                r1 = row[:]
                r1.pop(idx)
                if self.all_incr(r1):
                    return r1

                r2 = row[:]
                r2.pop(idx+1)
                if self.all_incr(r2):
                    return r2

                logging.debug('UNSAFE_INCR: %s', row)
                return False

        logging.debug('SAFE_INCR: %s', row)
        return row


    def all_decr(self, row):

        if len(row) < self.min_length:
            return False

        for idx in range(len(row) - 1):

            if row[idx] <= row[idx+1]:

                r1 = row[:]
                r1.pop(idx)
                if self.all_decr(r1):
                    return r1

                r2 = row[:]
                r2.pop(idx+1)
                if self.all_decr(r2):
                    return r2

                logging.debug('UNSAFE_DECR: %s', row)
                return False

        logging.debug('SAFE_DECR: %s', row)
        return row


    def safe_dist(self, row):

        if len(row) < self.min_length:
            return False

        for idx in range(len(row) - 1):

            diff = abs(row[idx] - row[idx+1])
            if (diff > 3 or diff < 1):

                r1 = row[:]
                r1.pop(idx)
                if self.safe_dist(r1):
                    return r1

                r2 = row[:]
                r2.pop(idx+1)
                if self.safe_dist(r2):
                    return r2

                logging.debug('UNSAFE_DIST: %s', row)
                return False

        logging.debug('SAFE_DIST: %s', row)
        return row


    def check_safety(self, tolerance=0):

        safe = 0

        for idx, row in enumerate(self.data):

            self.min_length = len(row) - tolerance
            logging.debug('ROW[%s]: %s', idx, row)

            incr = self.all_incr(row)

            if incr:
                row = incr
            else:
                decr = self.all_decr(row)

                if decr:
                    row = decr
                else:
                    logging.debug('X_UNSAFE_XXCR')
                    continue

            if not self.safe_dist(row):
                logging.debug('X_UNSAFE_DIST')
                continue

            safe += 1
            logging.debug('--SAFE--: %s', safe)

        logging.debug('%s SAFE out of %s', safe, len(self.data))
        return safe


def parse_args():

    parser = argparse.ArgumentParser(description='2024 Advent of Code, Day 2', epilog='https://adventofcode.com/2024')
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

    s = Safety(data_in)

    #test = [21, 20, 19, 17, 15, 12, 9, 8]
    #logging.debug(s.safe_dist(test, tolerance=1))
    #import sys
    #sys.exit()

    ##
    # Part 1
    if not conf.p2:
        start = time.time()
        sc = s.check_safety(tolerance=0)
        end = time.time()
        logging.info('[Part 1] Solution: %s in %s seconds', sc, round(end - start, 4))

    ##
    # Part 2
    if not conf.p1 or conf.p2:
        start = time.time()
        sc = s.check_safety(tolerance=1)
        end = time.time()
        logging.info('[Part 2] Solution: %s in %s seconds', sc, round(end - start, 4))

