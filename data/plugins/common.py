import os
import time
import json
import base64
import AutoUpdate

from pystyle import Write, Colors

__version__ = "2.0.9"
qotls = ["When the joke is a true fact/statement.", 
         "In the middle of every difficulty, lies opportunity.", 
         "If I'm the wire, can you be my socket <3", 
         "Dating 2 short girls isn't cheating, because half + half = 1", 
         "One does what he is told, never told what he does.",
]

# Clean and Pause variables
def cls():
    os.system('cls')

def pause():
    os.system('pause >nul')

# Updaters
def MainUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/Bloody%20Proxy%20Scraper%20V2.py")
    AutoUpdate.set_current_version(__version__)

    if not AutoUpdate.is_up_to_date():
        AutoUpdate.download("Bloody Proxy Scraper V2.py")

def CommonUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/data/plugins/common.py")
    AutoUpdate.set_current_version(__version__)

    if not AutoUpdate.is_up_to_date():
        AutoUpdate.download("common.py")

    os.remove("data/plugins/common.py")
    os.rename("common.py", "data/plugins/common.py")

def SkidUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/data/plugins/antiskid.py")
    AutoUpdate.set_current_version(__version__)

    if not AutoUpdate.is_up_to_date():
        AutoUpdate.download("antiskid.py")

    # directory = os.getcwd()
    os.remove("data/plugins/antiskid.py")
    os.rename("antiskid.py", "data/plugins/antiskid.py")

# Check if version.txt exists because you don't need it, it's needed for updating
def VersionFileRemover():
    versionfile = "data/version.txt"
    if os.path.isfile(versionfile):
        Write.Print("Detected version.txt, deleting (not needed on local pc)\n", Colors.red_to_yellow, interval=0)
        time.sleep(2)
        os.remove(versionfile)
        Write.Print("Deleted version.txt\n", Colors.green_to_blue, interval=0)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pass

def PythonInstallerDeleter():
    pythoninstaller = "tpython_installer.bat"
    if os.path.isfile(pythoninstaller):
        Write.Print("Detected Python installer, deleting (you already have Python)\n", Colors.red_to_yellow, interval=0)
        time.sleep(2)
        os.remove(pythoninstaller)
        Write.Print("Deleted Python installer\n", Colors.green_to_blue, interval=0)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        pass

def ChangelogsUpdater():
    changelogs = f"""Bloody Proxy Scraper v{__version__} Changelogs

Additions / Changes:
- Banner ASCII update
- Config update - Takes "true" and "True"
- Scrape cooldown (optional) - No decimals
- Most prints show time - Format H:M:S
- Shows current version instead of "V2"

Deletions:
- No deletions this update.
"""
    with open(f'data/changelogs-v{__version__}.txt', 'wb') as f:
        f.write(changelogs.encode('utf-8'))
        f.close
