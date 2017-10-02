#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import psutil

import conf
import utils


def cpu_percent(show_emblem=True, short=False):
    emblem = conf.EMBLEM['system']['cpu']
    color = conf.COLOR['cpu_percent']

    if short:
        label = "{0:.0f}".format(psutil.cpu_percent(conf.IO_INTERVAL))
    else:
        label = "{0:.1f}%".format(psutil.cpu_percent(conf.IO_INTERVAL))

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


def cpu_avg(show_emblem=True):
    emblem = conf.EMBLEM['system']['cpu']
    color = conf.COLOR['cpu_avg']

    # loadavg = os.getloadavg()
    # cores = psutil.cpu_count()
    # label = '{0:.1f}%'.format(loadavg[0] / cores * 100)
    label = "{0:.1f}".format(os.getloadavg()[0])

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print("{0} {1}".format(cpu_percent(), cpu_avg(False)))
