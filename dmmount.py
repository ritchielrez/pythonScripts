#!/usr/bin/python3

# Unmounting script for Linux 

import os
import subprocess
from rofi import Rofi

if __name__ == '__main__':
    r = Rofi(rofi_args=['-dpi', '1.25'])

    os.system('lsblk -l >> test')

    with open("test", "r") as ping:
        print(ping.read())