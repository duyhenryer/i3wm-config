#!/usr/bin/env python3

import gi
import subprocess
import sys

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class Response:
    CANCEL = 0
    LOGOUT = 1
    RESTART = 2
    SHUTDOWN = 3
    LOCK = 4

class ExitDialog(Gtk.MessageDialog):
    def __init__(self):
        super().__init__()
        msg = "Please choose an action."

        self.set_markup("<b><big>Exit</big></b>")
        self.format_secondary_text(msg)
        self.add_button("Cancel", Response.CANCEL)
        self.add_button("Logout", Response.LOGOUT)
        self.add_button("Restart", Response.RESTART)
        self.add_button("Shutdown", Response.SHUTDOWN)
        self.add_button("Lock", Response.LOCK)

        self.connect('delete-event', Gtk.main_quit)
        self.show_all()


def main():
    dialog = ExitDialog()
    response = dialog.run()

    if response == Response.LOGOUT:
        try:
            subprocess.call(['i3-msg', 'exit'])
        except subprocess.CalledProcessError:
            subprocess.call(['pkill', '-u', '$USER'])
    elif response == Response.SHUTDOWN:
        try:
            subprocess.call(['systemctl', 'poweroff'])
        except subprocess.CalledProcessError:
            subprocess.call(['shutdown', '-h', 'now'])
    elif response == Response.RESTART:
        try:
            subprocess.call(['systemctl', 'reboot'])
        except subprocess.CalledProcessError:
            subprocess.call(['reboot'])
    elif response == Response.LOCK:
        try: 
            subprocess.call(['/home/duyhenry/.config/i3/i3lock/i3lock.sh', 'i3lock'])
        except subprocess.CalledProcessError:
            subprocess.call(['i3lock'])

    dialog.destroy()
    sys.exit(0)

if __name__ == '__main__':
    main()
Gtk.main()




