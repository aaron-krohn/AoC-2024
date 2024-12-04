import re
import time
import logging
import argparse

import math
from functools import lru_cache
from pathlib import Path


class WordSearch:

    def __init__(self, raw_data):

        self.board = self.parse_raw(raw_data)

        self.masks = {
                'up': (-1, 0),
                'dn': (1, 0),
                'lt': (0, -1),
                'rt': (0, 1),
                'dul': (-1, -1),
                'dur': (-1, 1),
                'ddl': (1, -1),
                'ddr': (1, 1),
                }

        self.xmasks = {
                'dul': 'ddr',
                'dur': 'ddl',
                'ddl': 'dur',
                'ddr': 'dul',
                }


    def parse_raw(self, raw_data):

        rows = raw_data.split()

        return rows


    def count_words(self, word):

        total = 0

        for yidx, row in enumerate(self.board):

            for xidx in range(len(row)):

                for direction in self.masks:

                    if self.try_word(word, direction, (yidx, xidx)):
                        logging.debug('WORD')
                        total += 1

        return total


    def try_word(self, word, direction, start):

        logging.debug('TRY: %s %s %s', word, direction, start)

        x, y = (1, 0)

        sy = start[y]
        sx = start[x]

        if sy < 0 or sx < 0:
            return False

        try:
            letter = word[0] == self.board[sy][sx]
        except IndexError:
            return False

        mask = self.masks[direction]

        my = mask[y]
        mx = mask[x]

        ny = my + sy
        nx = mx + sx

        if letter:
            if len(word) == 1:
                return True

            return self.try_word(word[1:], direction, (ny, nx))

        return False


    def count_xwords(self, word):

        total = 0

        for yidx, row in enumerate(self.board):

            for xidx in range(len(row)):

                if self.try_xword(word, (yidx, xidx)):
                    total += 1

        return total


    def try_xword(self, word, start):

        wlen = len(word)
        if wlen % 2 == 0:
            return 0

        mid = int(len(word) / 2)

        total = 0

        for direction in ['dul', 'dur', 'ddl', 'ddr']:

            fhalf = word[0:mid+1][::-1]
            shalf = word[mid:]

            # Could potenitally optimize for cases where a known direction prevents
            # the opposite direction from being run if it hasn't been already
            if (self.try_word(fhalf, direction, start) and
                    self.try_word(shalf, self.xmasks[direction], start)):
                logging.debug('WORD')
                total += 1

        if total == 2:
            return True

        return False


def parse_args():

    parser = argparse.ArgumentParser(description='2024 Advent of Code, Day 4', epilog='https://adventofcode.com/2024')
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

    ws = WordSearch(data_in)

    ##
    # Part 1
    if not conf.p2:
        start = time.time()
        t = ws.count_words('XMAS')
        end = time.time()
        logging.info('[Part 1] Solution: %s in %s seconds', t, round(end - start, 4))

    ##
    # Part 2
    if not conf.p1 or conf.p2:
        start = time.time()
        t = ws.count_xwords('MAS')
        end = time.time()
        logging.info('[Part 2] Solution: %s in %s seconds', t, round(end - start, 4))

