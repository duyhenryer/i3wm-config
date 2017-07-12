#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import re
import subprocess

import conf
import utils


def battery(show_emblem=True, short=False, timeout=1):
    color = conf.COLOR['battery']

    # Read acpi output
    acpi_status = subprocess.check_output(
        ['acpi', '-b'], timeout=timeout
    ).strip().decode()

    if acpi_status:  # Output available (using battery)
        # Get status: (unknown, charging, discharging, full)
        re_status = re.search('(?<=: )\w+(?=,)', acpi_status)
        status = re_status.group()
        # Get percent
        re_percent = re.search('(?<=, )\d+(?=%)', acpi_status)

        percent = "{}".format(re_percent.group())

        if not short:
            percent += "%"

        if status == 'Unknown':  # Charged, Plugged in
            emblem = conf.EMBLEM['battery']['plugged']
            label = "{}".format(percent)
        elif status == 'Full':  # Full
            emblem = conf.EMBLEM['battery']['plugged']
            label = 'Full'
        else:  # Charging or discharged
            emblem = conf.EMBLEM['battery']['normal']
            label = "{}".format(percent)

            if status == "Charging":
                label = "+{}".format(label)
    else:  # Not using battery
        emblem = conf.EMBLEM['battery']['plugged']
        label = "A.C."

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print(battery())
