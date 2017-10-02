#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import subprocess

import conf
import utils


def mpd(show_emblem=True, timeout=1):
    color = conf.COLOR['mpd']

    try:
        mpc_output = subprocess.check_output([
            'mpc', '--format', conf.MPD_FORMAT,
            '--host', conf.MPD_HOST,
            '--port', conf.MPD_PORT
        ], timeout=timeout)
        mpd_status = mpc_output.decode().strip().split("\n")

        if len(mpd_status) == 3:  # Playing or paused
            label = mpd_status[0]

            if "playing" in mpd_status[1]:
                emblem = conf.EMBLEM['music']['playing']
            elif "paused" in mpd_status[1]:
                emblem = conf.EMBLEM['music']['paused']
            else:  # Unexpected case
                emblem = conf.EMBLEM['music']['default']
        else:  # Stopped
            emblem = conf.EMBLEM['music']['default']
            label = "N.A"
    except (subprocess.CalledProcessError, FileNotFoundError):
        emblem = conf.EMBLEM['music']['default']
        label = "N.A"

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)

if __name__ == '__main__':
    print(mpd())
