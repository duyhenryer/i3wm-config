#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import re
import subprocess

import conf
import utils


def xkb_indicator(show_emblem=True, timeout=1):
    emblem = conf.EMBLEM['system']['indicator']
    color = conf.COLOR['xkb_indicator']['active']

    label = ''
    xkb_status = subprocess.check_output(['xset', 'q'], timeout=timeout)

    numlock_status = re.search('(Num Lock: +)(on|off)', xkb_status.decode())
    capslock_status = re.search('(Caps Lock: +)(on|off)', xkb_status.decode())

    if numlock_status.group(2) == "on":
        num_color = conf.COLOR['xkb_indicator']['active']
    else:
        num_color = conf.COLOR['xkb_indicator']['inactive']

    label += utils.colorize(conf.EMBLEM['indicator']['numlock'], num_color)

    if capslock_status.group(2) == "on":
        caps_color = conf.COLOR['xkb_indicator']['active']
    else:
        caps_color = conf.COLOR['xkb_indicator']['inactive']

    label += utils.colorize(conf.EMBLEM['indicator']['capslock'], caps_color)

    if show_emblem:
        return "{0} {1}".format(utils.colorize(emblem, color), label)

    return label


if __name__ == '__main__':
    print(xkb_indicator())
