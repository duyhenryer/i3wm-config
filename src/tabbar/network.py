#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import re
import subprocess

import conf
import utils


def network(show_emblem=True, timeout=1):
    color = conf.COLOR['network']
    label = "Not Available"

    try:
        network_device = subprocess.check_output(
            ['nmcli', '-t', '-f', 'device,type,state,connection', 'device'],
            timeout=timeout
        )
        network_re = re.search('.*(ethernet|wifi).*:connected:.*',
                               network_device.decode())

        nm_device, nm_type, nm_state, nm_connection = \
            network_re.group(0).strip().split(":")
        label = nm_connection
    except (subprocess.CalledProcessError, FileNotFoundError, AttributeError):
        nm_type = None

    if os.path.isdir(conf.NETWORK_VPN_DIR):
        emblem = conf.EMBLEM['network']['protected']
    elif nm_type:
        if nm_type.strip() == "ethernet":
            emblem = conf.EMBLEM['network']['wired']
        elif nm_type.strip() == "wifi":
            emblem = conf.EMBLEM['network']['wireless']
        else:
            emblem = conf.EMBLEM['network']['unknown']
    else:
        emblem = conf.EMBLEM['network']['unknown']

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print(network())
