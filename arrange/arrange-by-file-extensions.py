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

for path in os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '').splitlines():
    if os.path.isdir(path) or os.path.islink(path):
        continue

    file_name = os.path.basename(path)
    name,file_ext = os.path.splitext(file_name)
    
    try:
        ext = file_ext.split('.')[1]
    except:
        continue

    if ext and ext is not "":
        target_dir = ext.upper()

    command1 = f'mkdir -p {target_dir}'
    command2 = f' mv "./{file_name}" "./{target_dir}/{file_name}"'

    run_command(command1)
    res = run_command(command2)
    if res == 0:
        pass
    else:
        err = err + 1

if err==0:
    notify('Files have been arranged by extensions','normal')
else:
    notify('Some files could not be arranged','critical')
