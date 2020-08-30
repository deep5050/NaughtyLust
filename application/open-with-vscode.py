#!/usr/bin/python3

import os
import subprocess


def notify(msg,level):
    try:
        command = f'notify-send -u {level} -t 2000 "NaughtyLust" "{msg}"'
        subprocess.Popen(command,shell=True)
    except:
        pass


def run_command(command):
    ret = 0
    try:
        out = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout, stderr = out.communicate()

        if stdout:
            ret = 0 # when no output checking is not necessary
        elif stderr:
            ret = 1
    except:
        return -1
    return ret


for path in os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '').splitlines():
    # open the first path
    # If some files are selected alongwith at least one directory
    # the directory will be selected
    command = f'code "{path}"'

    res  = run_command(command)
    if res == 0:
        notify('Opening in VScode','normal')
        break
    else:
        notify('Something went WRONG! could not open in VScode','critical')
        break