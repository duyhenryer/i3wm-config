#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import time

import conf
import utils


def clock(show_emblem=True, short=False):
    color = conf.COLOR['clock']

    if short:
        label = time.strftime(conf.TIME_FORMAT_SHORT)
    else:
        label = time.strftime(conf.TIME_FORMAT)

    hour = int(time.strftime("%I"))

    if hour == 12 or 0 < hour < 3:  # 12 1 2
        emblem = conf.EMBLEM['clock']['one_quarter']
    elif 3 <= hour < 6:  # 3 4 5
        emblem = conf.EMBLEM['clock']['two_quarter']
    elif 6 <= hour < 9:  # 6 7 8
        emblem = conf.EMBLEM['clock']['three_quarter']
    else:  # 9 10 11
        emblem = conf.EMBLEM['clock']['full']

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print(clock())
