#!/usr/bin/python3

# IMPORT MODULE

import youtube_dl
import os
import sys

# FUNCTION MP3 DOWNLOAD OR LISTEN

# if choice 1
def mp3down() :
    os.system("clear")
    os.system("cat banner")
    try:
       os.system('youtube-dl -x --audio-format mp3 -o "$HOME/downloads/%(title)s.%(ext)s" '+link)
       print("\033[0;32m download save in $HOME/downloads")
    except:
        os.system("clear")
        print("\033[0;31mERROR : failed to download")
        sys.exit()

# if choice 2
def mp3play() :
    os.system("clear")
    os.system("cat banner")
    loop = str(input("\033[0;33m looping or not (y/n) :"))
    if loop == "y" :
        os.system("clear")
        os.system("cat banner")
        os.system("mpv --loop-file "+playpath)
    elif loop == "n" :
        os.system("clear")
        os.system("cat banner")
        os.system("mpv "+playpath)
    else:
        os.system("mpv "+playpath)
# main code to run
def main() :
    global choice, link, playpath
    os.system("clear")
    os.system("cat banner")
    print("01 \033[0;35mdownload mp3 from youtube \033[0m")
    print("02 \033[0;35mplay music path folder")
    print(" ")
    choice = str(input("\033[0;32msellect \033[0m: "))
        
    if choice == '01':
       os.system("clear")
       os.system("cat banner")
       link = input("\033[0;34m link \033[0m: ")
       mp3down()
       sys.exit()

    elif choice == '02':
       os.system("clear")
       os.system("cat banner")
       playpath = input("\033[0;34mplaying path \033[0m: ")
       mp3play()
    else:
       print(str("\033[0;31m sellect error : "+choice))
main()





