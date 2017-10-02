#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import conf
import utils


if __name__ == '__main__':
    color = conf.COLOR['separator']
    symbol = conf.EMBLEM['misc']['separator']
    print(utils.colorize(symbol, color))
