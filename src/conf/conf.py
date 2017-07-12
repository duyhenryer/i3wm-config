#!/usr/bin/env python3

# MPD config
MPD_HOST = "XHv1OqE6Yy1oZbF5@127.0.0.1"
MPD_PORT = "2856"
MPD_FORMAT = "%title% - %artist%"

# HDDTEMP config
HDDTEMP_HOST = "127.0.0.1"
HDDTEMP_PORT = "7634"

# Net config
NETWORK_VPN_DIR = "/proc/sys/net/ipv4/conf/tun0"

# Sensor config
CPU_SENSOR_1 = '/sys/devices/platform/asus-nb-wmi/hwmon/hwmon1/temp1_input'
CPU_SENSOR_2 = '/sys/devices/platform/asus-nb-wmi/hwmon/hwmon2/temp1_input'

# Clock config
TIME_FORMAT = "%y:%m:%d %H:%M"
TIME_FORMAT_SHORT = "%H:%M"

# CPU / Disk / Network IO wait time
IO_INTERVAL = 1

# Check updates commands
PKG_COUNT_CMD = "pacman -Qq"
PKG_CHECK_UPDATE_CMD = "checkupdates"
PKG_CHECK_ORPHANED_CMD = "pacman -Qqdt"

# Color config

COLOR_DEF = {
    'black': '#FFFFFF',
    'white': '#ABB2BF',
    'red': '#E06C75',
    'green': '#98C379',
    'yellow': '#D19A66',
    'blue': '#61AFEF',
    'magenta': '#C678DD',
    'cyan': '#56B6C2',
    'gray': '#828997',
    'dark_gray': '#555555'
}

COLOR = {
    'battery': COLOR_DEF['red'],
    'check_updates': COLOR_DEF['magenta'],
    'clock': COLOR_DEF['cyan'],
    'cpu_avg': COLOR_DEF['yellow'],
    'cpu_percent': COLOR_DEF['yellow'],
    'cpu_temp': COLOR_DEF['red'],
    'disk_io': COLOR_DEF['blue'],
    'gpu_temp': COLOR_DEF['red'],
    'hdd_temp': COLOR_DEF['red'],
    'memory': COLOR_DEF['green'],
    'mpd': COLOR_DEF['gray'],
    'network': COLOR_DEF['magenta'],
    'network_io': COLOR_DEF['magenta'],
    'swap': COLOR_DEF['green'],
    'system_info': COLOR_DEF['white'],
    'volume': COLOR_DEF['blue'],
    'weather': COLOR_DEF['yellow'],
    'xkb_indicator': {
        'active': COLOR_DEF['yellow'],
        'inactive': COLOR_DEF['dark_gray']
    },

    'separator': COLOR_DEF['dark_gray'],
}

EMBLEM = {
    'battery': {
        'normal': '\U0001F50B',
        'plugged': '\U0001F50C'
    },
    'clock': {
        'full': '\u23fa',
        'one_quarter': '\u25d4',
        'two_quarter': '\u25d1',
        'three_quarter': '\u25d5',

        'first_quarter': '\u25f7',
        'second_quarter': '\u25f6',
        'third_quarter': '\u25f5',
        'fourth_quarter': '\u25f4',

        'first_triangle': '\u25e5',
        'second_triangle': '\u25e2',
        'third_triangle': '\u25e3',
        'fourth_triangle': '\u25e4',
    },
    'indicator': {
        'numlock': '[1]',
        'capslock': '[A]',
    },
    'music': {
        'default': '\U0000266B',
        'playing': '\u25B6',
        'paused': '\u23F8',
    },
    'network': {
        'wireless': '\U0001F4F6',
        'wired': '\u2693',
        'protected': '\U0001F512',
        'unknown': '\U0001F4F6'
    },
    'volume': {
        'high': '\U0001F50A',
        'medium': '\U0001F509',
        'low': '\U0001F508',
        'muted': '\U0001F507',
    },
    'system': {
        'computer': '\U0001F4BB',
        'cpu': '\u25A3',
        'disk': '\U0001F5AA',
        'memory': '\u25E8',
        'network': '\U0001F4F6',
        'package': '\U0001F4D6',
        'indicator': '\u2325',
    },
    'misc': {
        'arrow_up': '\u25B2',
        'arrow_down': '\u25BC',
        'temperature': '\U0001F375',
        'up-to-date': '\u2713',
        'separator': '/',
    }
}
