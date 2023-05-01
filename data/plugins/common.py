import os
import AutoUpdate
from pystyle import Write, Colors

# Updaters
def MainUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/Bloody%20Proxy%20Scraper%20V2.py")
    AutoUpdate.set_current_version("v2.0.7")

    if not AutoUpdate.is_up_to_date():
        Write.Print("Update found! Updating . . .\n", Colors.cyan_to_blue, interval=0)
        AutoUpdate.download("Bloody Proxy Scraper V2.py")

def CommonUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/data/plugins/common.py")
    AutoUpdate.set_current_version("v2.0.7")

    if not AutoUpdate.is_up_to_date():
        Write.Print("Update found for common.py! Updating . . .\n", Colors.cyan_to_blue, interval=0)
        AutoUpdate.download("common.py")

    os.remove("data/plugins/common.py")
    os.rename("common.py", "data/plugins/common.py")

def SkidUpdater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/data/plugins/antiskid.py")
    AutoUpdate.set_current_version("v2.0.7")

    if not AutoUpdate.is_up_to_date():
        Write.Print("Update found for antiskid.py! Updating . . .\n", Colors.cyan_to_blue, interval=0)
        AutoUpdate.download("antiskid.py")

    # directory = os.getcwd()
    os.remove("data/plugins/antiskid.py")
    os.rename("antiskid.py", "data/plugins/antiskid.py")
