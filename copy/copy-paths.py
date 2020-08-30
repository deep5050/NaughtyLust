#!/usr/bin/python3

import os
import subprocess


def notify(msg,level):
    try:
        command = f'notify-send -u {level} -t 2000 "NaughtyLust" "{msg}"'
        subprocess.Popen(command,shell=True)
    except:
        pass



try:
    import pyperclip
except ImportError as e:
    notify('Sorry, pyperclip is not installed, run pip3 install pyperclip','critical')
    exit(1)


path = os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '')

path = path.strip()
if path is not "":
    try:
        pyperclip.copy(path)
        notify('Paths have been saved to clipboard','normal')
    except:
        notify('Something went WRONG! could not add paths to clipboard','critical')
