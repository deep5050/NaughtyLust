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


URIs = os.getenv('NAUTILUS_SCRIPT_SELECTED_URIS', '')
URIs = URIs.strip()

if URIs is not "":
    try:
        pyperclip.copy(URIs)
        notify('URIs have been added to clipboard','normal')
    except:
        notify('Something went WRONG! could not save to clipboard','critical')