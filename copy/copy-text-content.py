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

text_ext = types = {"ogm":"video","class":"code","js":"code","swift":"code","cc":"code","tga":"image","ape":"audio","woff2":"font","cab":"archive","whl":"archive","mpe":"video","rmvb":"video","srt":"video","xz":"archive","exe":"exec","m4a":"audio","crx":"exec","vob":"video","tif":"image","gz":"archive","roq":"video","m4v":"video","gif":"image","rb":"code","3g2":"video","m4":"code","ar":"archive","vb":"code","sid":"audio","ai":"image","wma":"audio","pea":"archive","bmp":"image","py":"code","mp4":"video","m4p":"video","ods":"sheet","jpeg":"image","command":"exec","azw4":"book","otf":"font","ttf":"font","mobi":"book","ra":"audio","flv":"video","ogv":"video","mpg":"video","xls":"sheet","jpg":"image","mkv":"video","nsv":"video","mp3":"audio","kmz":"image","java":"code","lua":"code","m2v":"video","deb":"archive","csv":"sheet","pls":"audio","pak":"archive","egg":"archive","tlz":"archive","c":"code","cbz":"book","xcodeproj":"code","iso":"archive","xm":"audio","azw":"book","webm":"video","3ds":"image","azw6":"book","azw3":"book","php":"code","kml":"image","woff":"font","log":"text","zipx":"archive","3gp":"video","po":"code","mpa":"audio","mng":"video","a":"archive","s7z":"archive","ics":"sheet","tex":"text","go":"code","ps":"image","org":"text","sh":"exec","msg":"text","xml":"code","cpio":"archive","epub":"book","lha":"archive","flac":"audio","odp":"slide","wmv":"video","vcxproj":"code","mar":"archive","eot":"font","less":"web","asf":"video","apk":"archive","css":"web","mp2":"video","patch":"code","wav":"audio","msi":"exec","rs":"code","gsm":"audio","ogg":"video","cbr":"book","azw1":"book","m":"code","dds":"image","h":"code","dmg":"archive","mid":"audio","psd":"image","dwg":"image","aac":"audio","s3m":"audio","cs":"code","cpp":"code","au":"audio","aiff":"audio","diff":"code","avi":"video","bat":"exec","html":"code","bin":"exec","txt":"text","rpm":"archive","m3u":"audio","max":"image","vcf":"sheet","svg":"image","ppt":"slide","clj":"code","png":"image","svi":"video","tiff":"image","tgz":"archive","mxf":"video","7z":"archive","drc":"video","yuv":"video","mov":"video","tbz2":"archive","bz2":"archive","gpx":"image","shar":"archive","xcf":"image","dxf":"image","jar":"archive","qt":"video","tar":"archive","xpi":"archive","zip":"archive","thm":"image","cxx":"code","3dm":"image","rar":"archive","md":"text","scss":"web","mpv":"video","webp":"image","war":"archive","pl":"code","xlsx":"sheet","mpeg":"video","aaf":"video","avchd":"video","mod":"audio","rm":"video","it":"audio","wasm":"web","el":"code","eps":"image"}


for path in os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '').splitlines():

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
            content = f.readlines()
            f.close()
            s = ""
            s = s.join(content)
            # print(s)
            pyperclip.copy(s.strip())
            notify('Content saved to clipboard','normal')
            break
        except:
            notify('Something went WRONG! could not save content to clipboard','critical')
            break