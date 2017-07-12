#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import time
import psutil

import conf
import utils


def disk_io(show_emblem=True):
    emblem = conf.EMBLEM['system']['disk']
    color = conf.COLOR['disk_io']

    # get raw disk io
    pre_io = psutil.disk_io_counters()
    time.sleep(conf.IO_INTERVAL)
    pos_io = psutil.disk_io_counters()

    # calc net disk io time
    net_read_time = pos_io[4] - pre_io[4]
    net_write_time = pos_io[5] - pre_io[5]

    try:
        disk_read_bytes = (pos_io[2] - pre_io[2]) * (1 / net_read_time)
        disk_read = utils.convert_unit(disk_read_bytes)
    except ZeroDivisionError:
        disk_read = "0B"

    try:
        disk_write_bytes = (pos_io[3] - pre_io[3]) * (1 / net_write_time)
        disk_write = utils.convert_unit(disk_write_bytes)
    except ZeroDivisionError:
        disk_write = "0B"

    label = '{2}{0: >6} {3}{1: >6}'.format(disk_read, disk_write,
                                           conf.EMBLEM['misc']['arrow_up'],
                                           conf.EMBLEM['misc']['arrow_down'])
    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)

if __name__ == '__main__':
    print(disk_io())
