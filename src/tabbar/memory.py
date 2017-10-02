#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import psutil

import conf
import utils


def memory(show_emblem=True):
    emblem = conf.EMBLEM['system']['memory']
    color = conf.COLOR['memory']

    mem = psutil.virtual_memory().total - psutil.virtual_memory().available
    label = utils.convert_unit(mem)

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


def swap(show_emblem=True):
    emblem = conf.EMBLEM['system']['memory']
    color = conf.COLOR['swap']

    swp = psutil.swap_memory().used
    label = utils.convert_unit(swp)

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print("{0} {1}".format(memory(), swap(False)))
