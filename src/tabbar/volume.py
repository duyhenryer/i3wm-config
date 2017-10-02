#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import re
import subprocess

import conf
import utils


def volume(show_emblem=True, short=False, timeout=1):
    color = conf.COLOR['volume']

    amixer = subprocess.check_output(['amixer', 'get', 'Master'],
                                     timeout=timeout)

    if re.search("\[on\]", amixer.decode()):  # Volume is on
        re_vol = re.search('(?<=\[)\d+(?=%\])', amixer.decode())
        vol_percent = int(re_vol.group())

        if vol_percent > 60:
            emblem = conf.EMBLEM['volume']['high']
        elif vol_percent > 30:
            emblem = conf.EMBLEM['volume']['medium']
        else:
            emblem = conf.EMBLEM['volume']['low']

        label = "{}".format(vol_percent)

        if not short:
            label += "%"
    else:  # Volume is off
        emblem = conf.EMBLEM['volume']['muted']
        label = 'off'

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print(volume())
