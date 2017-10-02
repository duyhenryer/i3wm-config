#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import re
import subprocess

import conf
import utils


def system_info(show_emblem=True, short=False, timeout=1):
    emblem = conf.EMBLEM['system']['computer']
    color = conf.COLOR['system_info']

    if short:
        return utils.colorize("Arch Linux".upper(), color)

    # get OS name
    try:
        os_release = open('/etc/os-release').read()
        name = re.search('(?<=NAME=").*(?=")', os_release).group(0)
    except (FileNotFoundError, FileExistsError):
        name = "Linux"

    label = "{0} {1}".format(
        name, subprocess.check_output(['uname', '-r'],
                                      timeout=timeout).decode().strip()
    )

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print(system_info())
