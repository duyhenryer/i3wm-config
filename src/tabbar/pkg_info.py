#!/usr/bin/env python3

import os
os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

import subprocess

import conf
import utils


def check_updates(show_emblem=True):
    emblem = conf.EMBLEM['system']['package']
    color = conf.COLOR['check_updates']

    packages_count = None
    packages_outdated = None
    packages_orphaned = None

    # Get packages count
    try:
        proc = subprocess.check_output(conf.PKG_COUNT_CMD.split()).strip()
        packages_count = len(proc.decode().split('\n'))
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Get oudated packages
    try:
        proc = subprocess.check_output(
            conf.PKG_CHECK_UPDATE_CMD.split()
        ).strip()

        if proc:
            packages_outdated = "{}".format(len(proc.decode().split('\n')))
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Get orphaned packages
    try:
        proc = subprocess.check_output(
            conf.PKG_CHECK_ORPHANED_CMD.split()
        ).strip()

        if proc:
            packages_orphaned = "{}".format(len(proc.decode().split('\n')))
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Format label
    if packages_outdated:
        if packages_orphaned:
            label = '{0} (+{1} -{2})'.format(
                packages_count, packages_outdated, packages_orphaned
            )
        else:
            label = '{0} (+{1})'.format(packages_count, packages_outdated)
    else:
        if packages_orphaned:
            label = '{0}{1} (-2)'.format(
                packages_count, conf.EMBLEM['misc']['up-to-date'],
                packages_orphaned
            )
        else:
            label = '{}'.format(packages_count)

    if show_emblem:
        return utils.colorize("{0} {1}".format(emblem, label.upper()), color)

    return utils.colorize(label.upper(), color)


if __name__ == '__main__':
    print(check_updates())
