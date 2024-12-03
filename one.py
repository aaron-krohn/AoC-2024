import time
import logging
import argparse

import math
from functools import lru_cache
from pathlib import Path

class LocationDistances:

    def __init__(self, raw_data):

        self.left, self.right = self.parse_raw(raw_data)


    def parse_raw(self, raw):

        rose = raw.split('\n')

        left = []
        right = []

        for row in rose:
            logging.debug(row)

            leftright = row.split(' ')
            logging.debug(leftright)

            if leftright[0] and leftright[-1]:
                left.append(int(leftright[0]))
                right.append(int(leftright[-1]))

        return left, right


    def total_distance(self):

        left = self.left[:]
        right = self.right[:]

        left.sort()
        right.sort()

        dist = 0

        for idx in range(len(left)):

            dist += abs(left[idx] - right[idx])

        return dist


    def similarity_score(self):

        left = self.left[:]
        right = self.right[:]

        left.sort()
        right.sort()

        rights = {}

        sim = 0

        for r in right:
            rights.setdefault(r, 0)
            rights[r] += 1

        for l in left:

            times = 0

            try:
                sim += l * rights[l]
            except KeyError:
                continue

        return sim



def parse_args():

    parser = argparse.ArgumentParser(description='2024 Advent of Code, Day 1', epilog='https://adventofcode.com/2024')
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

    lc = LocationDistances(data_in)

    ##
    # Part 1
    if not conf.p2:
        start = time.time()
        d = lc.total_distance()
        end = time.time()
        logging.info('[Part 1] Solution: %s in %s seconds', d, round(end - start, 4))

    ##
    # Part 2
    if not conf.p1 or conf.p2:
        start = time.time()
        s = lc.similarity_score()
        end = time.time()
        logging.info('[Part 2] Solution: %s in %s seconds', s, round(end - start, 4))

