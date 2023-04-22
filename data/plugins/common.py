import AutoUpdate

# Updater
def Updater():
    AutoUpdate.set_url("https://github.com/NoobToolzz/Bloody-Proxy-Scraper/blob/main/data/version.txt")
    AutoUpdate.set_download_link("https://raw.githubusercontent.com/NoobToolzz/Bloody-Proxy-Scraper/main/Bloody%20Proxy%20Scraper%20V2.py")
    AutoUpdate.set_current_version("v2.0.4")

    if not AutoUpdate.is_up_to_date():
        AutoUpdate.download("Bloody Proxy Scraper V2.py")
