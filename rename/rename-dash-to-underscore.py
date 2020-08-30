#!/usr/bin/python3

import os
import subprocess

def run_command(command):
    ret = 0
    try:
        out = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        print(command)
        stdout, stderr = out.communicate()

        if stdout:
            ret = 0 # when no output checking is not necessary
        elif stderr:
            ret = 1
    except:
        return -1
    return ret


def notify(msg,level):
    try:
        command = f'notify-send -u {level} -t 2000 "NaughtyLust" "{msg}"'
        subprocess.Popen(command,shell=True)
    except:
        pass

err = 0

for path in os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS','').splitlines():
    new_path = path.strip()
    new_path = new_path.replace('-','_')
    command = f' mv "{path}" "{new_path}"'
    
    res = run_command(command)
    if res == 0:
        pass
    else:
        err = err + 1

if err == 0:
    notify('All files renamed','normal')
else:
    notify('Some renaming failed','critical')