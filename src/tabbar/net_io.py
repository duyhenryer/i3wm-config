#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import time
import psutil

import conf
import utils


def network_io(show_emblem=True):
    emblem = conf.EMBLEM['system']['network']
    color = conf.COLOR['network_io']

    try:
        time_ratio = 1 / conf.IO_INTERVAL
    except ZeroDivisionError:
        time_ratio = 1

    # get raw net io
    pre_io = psutil.net_io_counters()
    time.sleep(conf.IO_INTERVAL)
    pos_io = psutil.net_io_counters()

    # calculate net io
    net_sent_bytes = pos_io[0] - pre_io[0]
    net_recv_bytes = pos_io[1] - pre_io[1]

    # convert to higher unit
    net_sent = utils.convert_unit(net_sent_bytes * time_ratio)
    net_recv = utils.convert_unit(net_recv_bytes * time_ratio)

    label = '{2}{0: >6} {3}{1: >6}'.format(net_sent, net_recv,
                                           conf.EMBLEM['misc']['arrow_up'],
                                           conf.EMBLEM['misc']['arrow_down'])

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)

if __name__ == '__main__':
    print(network_io())
