#!/usr/bin/env python3


def convert_unit(bytes_=0, unit_size=1024):
    result = "0B"

    for s in ['B', 'K', 'M', 'G', 'T', 'P']:
        if bytes_ < unit_size:
            result = "{0:.1f}{1}".format(bytes_, s)
            break
        else:
            bytes_ /= unit_size

    return result


def colorize(text, color):
    return '<span color="{1}">{0}</span>'.format(text, color)
