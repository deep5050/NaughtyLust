#!/usr/bin/python3

import os
import subprocess


image_formats = ['jpg', 'jpeg', 'png']

def run_command(command):
    try:
        out = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        stdout, stderr = out.communicate()

        if (stdout):
            return 0
        if(stderr):
            return 1
    except:
        return -1


def notify(msg,level):
    try:
        command = f'notify-send -u {level} -t 2000 "NaughtyLust" "{msg}"'
        subprocess.Popen(command,shell=True)
    except:
        pass


for path in os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '').splitlines():
    if os.path.isfile(path):
        file_name = os.path.basename(path)
        file_name = file_name.strip()
        if any(ext in file_name for ext in image_formats):
            command = f'gsettings set org.gnome.desktop.screensaver picture-uri "file://{path}"'
            res = run_command(command)
            if res == 0:
                notify('Lockscreen Image has been changed','normal')
                break
            else:
                notify('Could not set lockscreen image','critical')
