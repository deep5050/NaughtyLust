#!/usr/bin/python3

import os
import sys
import json
import subprocess


def notify(msg, level):
    try:
        command = f'notify-send -u {level} -t 2000 "NaughtyLust" "{msg}"'
        subprocess.Popen(command, shell=True)
    except:
        pass


try:
    import requests
    import pyperclip
except ImportError as e:
    notify('Sorry, make sure requests and pyperclip is installed', 'critical')
    exit(1)



################################## Enter you  user credentials   Here  ######################
user_name = 'USERNAME'
password_or_access_token = 'PASSWORD/TOKEN'
#########################################################################################


def upload_gist(to_upload):
    global user_name
    global password_or_access_token

    try:
        r = requests.post('https://api.github.com/gists',json.dumps(
            {"description": "NaughtyLust upload","public": False,'files':to_upload})
            ,auth=requests.auth.HTTPBasicAuth(user_name, password_or_access_token))

        response = r.json()

        try:
            if response['html_url']:
                url = response['html_url']
                try:
                    pyperclip.copy(url.strip())
                    notify(f'URL copied to clipboard','normal')
                    exit(0)
                except:
                    notify(f'Uploaded to {url} successfully','normal')
                    exit(0)
        except:
            pass

        try:
            if response['message']:
                msg = response['message']

                if msg == "Bad credentials":
                    notify('Enter correct username or password/token','critical')
                    exit(1)
                
                if msg == 'Must specify two-factor authentication OTP code.':
                    notify('Use Your personal access token instead of password','critical')
                    exit(1)
        except:
            pass

    except:
        notify('Sorry something went WRONG!','critical')
        exit(1)




   
types = {"ogm":"video","class":"code","js":"code","swift":"code","cc":"code","tga":"image","ape":"audio","woff2":"font","cab":"archive","whl":"archive","mpe":"video","rmvb":"video","srt":"video","xz":"archive","exe":"exec","m4a":"audio","crx":"exec","vob":"video","tif":"image","gz":"archive","roq":"video","m4v":"video","gif":"image","rb":"code","3g2":"video","m4":"code","ar":"archive","vb":"code","sid":"audio","ai":"image","wma":"audio","pea":"archive","bmp":"image","py":"code","mp4":"video","m4p":"video","ods":"sheet","jpeg":"image","command":"exec","azw4":"book","otf":"font","ttf":"font","mobi":"book","ra":"audio","flv":"video","ogv":"video","mpg":"video","xls":"sheet","jpg":"image","mkv":"video","nsv":"video","mp3":"audio","kmz":"image","java":"code","lua":"code","m2v":"video","deb":"archive","csv":"sheet","pls":"audio","pak":"archive","egg":"archive","tlz":"archive","c":"code","cbz":"book","xcodeproj":"code","iso":"archive","xm":"audio","azw":"book","webm":"video","3ds":"image","azw6":"book","azw3":"book","php":"code","kml":"image","woff":"font","log":"text","zipx":"archive","3gp":"video","po":"code","mpa":"audio","mng":"video","a":"archive","s7z":"archive","ics":"sheet","tex":"text","go":"code","ps":"image","org":"text","sh":"code","msg":"text","xml":"code","cpio":"archive","epub":"book","lha":"archive","flac":"audio","odp":"slide","wmv":"video","vcxproj":"code","mar":"archive","eot":"font","less":"web","asf":"video","apk":"archive","css":"web","mp2":"video","patch":"code","wav":"audio","msi":"exec","rs":"code","gsm":"audio","ogg":"video","cbr":"book","azw1":"book","m":"code","dds":"image","h":"code","dmg":"archive","mid":"audio","psd":"image","dwg":"image","aac":"audio","s3m":"audio","cs":"code","cpp":"code","au":"audio","aiff":"audio","diff":"code","avi":"video","bat":"code","html":"code","bin":"exec","txt":"text","rpm":"archive","m3u":"audio","max":"image","vcf":"sheet","svg":"image","ppt":"slide","clj":"code","png":"image","svi":"video","tiff":"image","tgz":"archive","mxf":"video","7z":"archive","drc":"video","yuv":"video","mov":"video","tbz2":"archive","bz2":"archive","gpx":"image","shar":"archive","xcf":"image","dxf":"image","jar":"archive","qt":"video","tar":"archive","xpi":"archive","zip":"archive","thm":"image","cxx":"code","3dm":"image","rar":"archive","md":"text","scss":"web","mpv":"video","webp":"image","war":"archive","pl":"code","xlsx":"sheet","mpeg":"video","aaf":"video","avchd":"video","mod":"audio","rm":"video","it":"audio","wasm":"web","el":"code","eps":"image"}

contents_to_upload = {}
for path in os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '').splitlines():
    print(path)
    if os.path.isdir(path) or os.path.islink(path):
        continue
    file_name = os.path.basename(path)
    name,file_ext = os.path.splitext(file_name)
    
    try:
        ext = file_ext.split('.')[1]
    except:
        # could not decide this one, continue
        continue

    if ext and ext is not "":
        try:
            check_ext = types.get(ext.lower())
        except:
            continue
        
    if check_ext == 'text' or check_ext=='code':
        # read the content, save to clipboard and quit
        try:
            f = open(path,'r')
            content = f.read()
            f.close()
            contents_to_upload[file_name] = {"content": content}  
        except:
            notify('Something went WRONG!','critical')
            exit(1)
   
   
upload_gist(contents_to_upload)