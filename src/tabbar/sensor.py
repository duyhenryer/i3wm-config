#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import re
import subprocess

import conf
import utils


def cpu_temp(show_emblem=True, short=False):
    emblem = conf.EMBLEM['misc']['temperature']
    color = conf.COLOR['cpu_temp']

    try:
        sensor = open(conf.CPU_SENSOR_1).read()

        if short:
            label = "{:.0f}".format(int(sensor) / 1000)
        else:
            label = "{:.0f}°C".format(int(sensor) / 1000)
    except (FileNotFoundError, FileExistsError):
        try:
            sensor = open(conf.CPU_SENSOR_2).read()

            if short:
                label = "{:.0f}".format(int(sensor) / 1000)
            else:
                label = "{:.0f}°C".format(int(sensor) / 1000)
        except (FileExistsError, FileNotFoundError):
            label = "N.A"

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


def gpu_temp(show_emblem=True, short=False, timeout=2):
    emblem = conf.EMBLEM['misc']['temperature']
    color = conf.COLOR['gpu_temp']

    try:
        sensor = subprocess.check_output(
            ['nvidia-smi', '-q', '-d', 'temperature'], timeout=timeout
        )
        re_sensor = re.search('(?<=GPU Current Temp).*(\d+)(?= C)',
                              sensor.decode())
        label = re.search('\d+', re_sensor.group()).group()

        if not short:
            label += "°C"
    except (subprocess.CalledProcessError, FileNotFoundError):
        label = 'N.A'

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


def hdd_temp(show_emblem=True, short=False, timeout=2):
    emblem = conf.EMBLEM['misc']['temperature']
    color = conf.COLOR['hdd_temp']

    try:
        sensor = subprocess.check_output(
            ['telnet', conf.HDDTEMP_HOST, conf.HDDTEMP_PORT], timeout=timeout
        ).strip()
        re_sensor = re.search('(?<=\|)\d+(?=|C)', sensor.decode())
        label = re_sensor.group()

        if not short:
            label += '°C'
    except (subprocess.CalledProcessError, FileNotFoundError):
        label = "N.A"

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print("{0} {1}".format(cpu_temp(), gpu_temp(False)))
