import os, time, requests, pystyle, random, datetime, json

from pystyle import Write, Colors, Colorate, Center
from console.utils import set_title
from colorama import Fore

from data.sources import http_urls, socks4_urls, socks5_urls, all_urls
from data.plugins.common import cls, pause, MainUpdater, CommonUpdater, SkidUpdater, VersionFileRemover, ChangelogsUpdater, CurrentVersion
from data.plugins.antiskid import AntiSkid
from win10toast import ToastNotifier
toast = ToastNotifier()
cls()

# Load Configuration
config = json.load(open('config.json', 'r', encoding='utf-8'))

# Check if version.txt exists. If it does, delete it.
VersionFileRemover()

# Check for updates to main file, and both files in data/plugins
print(f"{Fore.YELLOW}[{Fore.RESET}INFO{Fore.YELLOW}]{Fore.RESET} Checking for updates . . .")
# MainUpdater()
print(f"{Fore.GREEN}[{Fore.RESET}SUCCESS{Fore.GREEN}]{Fore.RESET} Updated main file")
time.sleep(0.5)
CommonUpdater()
print(f"{Fore.GREEN}[{Fore.RESET}SUCCESS{Fore.GREEN}]{Fore.RESET} Updated data/plugins/common.py")
time.sleep(0.5)
SkidUpdater()
print(f"{Fore.GREEN}[{Fore.RESET}SUCCESS{Fore.GREEN}]{Fore.RESET} Updated data/plugins/antiskid.py")

# Writes changelogs to changelogs.txt in data folder
ChangelogsUpdater()
print(f"{Fore.GREEN}[{Fore.RESET}INFO{Fore.GREEN}]{Fore.RESET} Written changelogs to data/changelogs.txt")
time.sleep(2)

# Anti-Skid
__author__ = 'NoNoobz'

if __author__ != '\u004E\u006F\u004E\u006F\u006F\u0062\u007A':
    AntiSkid()

h_h2 = ["Halal", "Haram"]
now = datetime.datetime.now()
timenow = now.strftime("%H:%M:%S")

cls()
# os.system('mode 85, 25')
banner = f"""
██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝███████╗
██╔══██╗██╔═══╝ ╚════██║
██████╔╝██║     ███████║
╚═════╝ ╚═╝     ╚══════╝ v{CurrentVersion}                        
Made by {__author__}
This program is {random.choice(h_h2)}
Started at: {timenow}
"""
if config["notifications"] == "true" or config["notifications"] == "True":
    toast.show_toast(f"Bloody Proxy Scraper v{CurrentVersion}",
                     "Started to scrape proxies.",
                     icon_path="data\icons\logo.ico",
                     duration=2)
else:
    pass
Write.Print("------------------------------------------------------------------------------------------------------------------------", Colors.purple_to_blue, interval=0)
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
Write.Print("------------------------------------------------------------------------------------------------------------------------", Colors.rainbow, interval=0)
time.sleep(1)
optional_cooldown = Write.Input("Do you want a cooldown between each scrape? (y/n): ", Colors.purple_to_blue, interval=0)
if optional_cooldown == "y" or optional_cooldown == "Y" or optional_cooldown == "yes" or optional_cooldown == "Yes" or optional_cooldown == "YES":
    Write.Print("\n[WARNING] Do not put any decimals in the cooldown\n", Colors.red_to_yellow, interval=0)
    cooldown_input = Write.Input("How much do you want the cooldown to be? (in seconds): ", Colors.purple_to_blue, interval=0)
    if "." in cooldown_input:
        Write.Print("\nDetected a decimal in the cooldown, removing\n", Colors.red_to_yellow, interval=0)
        cooldown = cooldown_input.replace(".", "")
        Write.Print(f"New cooldown: {cooldown}\n", Colors.green_to_white, interval=0)
    if "0." in cooldown_input:
        Write.Print("\nDetected a decimal in the cooldown, removing\n", Colors.red_to_yellow, interval=0)
        cooldown = cooldown_input.replace("0.", "")
        Write.Print(f"New cooldown: {cooldown}\n", Colors.green_to_white, interval=0)
else:
    pass
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.rainbow, interval=0)
set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraping Proxies . . .")
Write.Print("[?] Scraping Proxies . . .\n", Colors.red_to_yellow, interval=0)

# Opening/Adding proxy 
# Edit: Proxy files are opened when proxies are being written. You can safely remove the #'s below without errors if you wish.
# http = open('proxies-http.txt','wb')
# socks4 = open('proxies-socks4.txt','wb')
# socks5 = open('proxies-socks5.txt','wb')
# allp = open('proxies-all.txt','wb')
# scraped_sites = 0

# Scrape HTTP(s) proxies from their sources 
http_proxies = []
for url in http_urls:
    try:
        scrape_http = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped HTTP Proxies from {url}!")
        Write.Print(f"\n[{timenow}] | [?] Scraped HTTP Proxies from {url}\n", Colors.green_to_blue, interval=0)
        http_proxies.extend(scrape_http.text.strip().split('\n'))
        if optional_cooldown == "y" or optional_cooldown == "Y" or optional_cooldown == "yes" or optional_cooldown == "Yes" or optional_cooldown == "YES":
            time.sleep(int(cooldown))
        else:
            pass
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[{timenow}] | [!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped HTTP Proxies!")
Write.Print(f"[{timenow}] | [?] Scraped HTTP(S) Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.rainbow, interval=0)
if config["notifications"] == "true" or config["notifications"] == "True":
    toast.show_toast(f"Bloody Proxy Scraper v{CurrentVersion}",
                     "Scraped HTTP(S) Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
else:
    pass
time.sleep(1)

# Scrape SOCKS4 proxies from their sources
socks4_proxies = []
for url in socks4_urls:
    try:
        scrape_socks4 = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped SOCKS4 Proxies from {url}!")
        Write.Print(f"\n[{timenow}] | [?] Scraped SOCKS4 Proxies from {url}\n", Colors.green_to_blue, interval=0)
        socks4_proxies.extend(scrape_socks4.text.strip().split('\n'))
        if optional_cooldown == "y" or optional_cooldown == "Y" or optional_cooldown == "yes" or optional_cooldown == "Yes" or optional_cooldown == "YES":
            time.sleep(int(cooldown))
        else:
            pass
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[{timenow}] | [!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped SOCKS4 Proxies!")
Write.Print(f"[{timenow}] | [?] Scraped SOCKS4 Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.rainbow, interval=0)
if config["notifications"] == "true" or config["notifications"] == "True":
    toast.show_toast(f"Bloody Proxy Scraper v{CurrentVersion}",
                     "Scraped SOCKS4 Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
else:
    pass
time.sleep(1)

# Scrape SOCKS5 proxies from their sources
socks5_proxies = []
for url in socks5_urls:
    try:
        scrape_socks5 = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped SOCKS5 Proxies from {url}!")
        Write.Print(f"\n[{timenow}] | [?] Scraped SOCKS5 Proxies from {url}\n", Colors.green_to_blue, interval=0)
        socks5_proxies.extend(scrape_socks5.text.strip().split('\n'))
        if optional_cooldown == "y" or optional_cooldown == "Y" or optional_cooldown == "yes" or optional_cooldown == "Yes" or optional_cooldown == "YES":
            time.sleep(int(cooldown))
        else:
            pass
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[{timenow}] | [!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped SOCKS5 Proxies!")
Write.Print(f"[{timenow}] | [?] Scraped SOCKS5 Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.rainbow, interval=0)
if config["notifications"] == "true" or config["notifications"] == "True":
    toast.show_toast(f"Bloody Proxy Scraper v{CurrentVersion}",
                     "Scraped SOCKS5 Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
else:
    pass
time.sleep(1)

# Scrape ALL proxies from their sources
all_proxies = []
for url in all_urls:
    try:
        scrape_all = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped ALL Proxies from {url}!")
        Write.Print(f"\n[{timenow}] | [?] Scraped ALL Proxies from {url}\n", Colors.green_to_blue, interval=0)
        all_proxies.extend(scrape_all.text.strip().split('\n'))
        if optional_cooldown == "y" or optional_cooldown == "Y" or optional_cooldown == "yes" or optional_cooldown == "Yes" or optional_cooldown == "YES":
            time.sleep(int(cooldown))
        else:
            pass
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[{timenow}] | [!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Scraped ALL Proxies!")
Write.Print(f"[{timenow}] | [?] Scraped ALL Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.rainbow, interval=0)
if config["notifications"] == "true" or config["notifications"] == "True":
    toast.show_toast(f"Bloody Proxy Scraper v{CurrentVersion}",
                     "Scraped ALL Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
else:
    pass
time.sleep(1)

set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Finished Scraping Proxies!")
Write.Print(f"[{timenow}] | [!] Finished Scraping Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.rainbow, interval=0)
time.sleep(1)
set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Writing Proxies . . .")
Write.Print(f"[{timenow}] | [?] Writing Proxies In Files . . .\n\n", Colors.red_to_yellow, interval=0)
if config["notifications"] == "true" or config["notifications"] == "True":
    toast.show_toast(f"Bloody Proxy Scraper v{CurrentVersion}",
                     "Writing Proxies...",
                     icon_path="data\icons\logo.ico",
                     duration=1)
else:
    pass
time.sleep(1)

# Writing Proxies In Their Files

# Write HTTP(s) proxies to file
with open('proxies-http.txt','wb') as http:
    for proxy in http_proxies:
        http.write(proxy.encode('utf-8') + b'\n')
Write.Print(f"[{timenow}] | [?] Wrote HTTP Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

# Write SOCKS4 proxies to file
with open('proxies-socks4.txt','wb') as socks4:
    for proxy in socks4_proxies:
        socks4.write(proxy.encode('utf-8') + b'\n')
Write.Print(f"[{timenow}] | [?] Wrote SOCKS4 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

# Write SOCKS5 proxies to file
with open('proxies-socks5.txt','wb') as socks5:
    for proxy in socks5_proxies:
        socks5.write(proxy.encode('utf-8') + b'\n')
Write.Print(f"[{timenow}] | [?] Wrote SOCKS5 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

with open('proxies-all.txt','wb') as allp:
    for proxy in all_proxies:
        allp.write(proxy.encode('utf-8') + b'\n')
Write.Print(f"[{timenow}] | [?] Wrote ALL Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Wrote Proxies!")
Write.Print(f"[{timenow}] | [!] Finished Writing Proxies In Files!\n", Colors.green_to_white, interval=0)
Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.rainbow, interval=0)
time.sleep(0.5)

set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Closing Files . . .")
Write.Print(f"[{timenow}] | [?] Closing Files . . .\n", Colors.red_to_yellow, interval=0)
time.sleep(0.5)

# Closing Files
http.close()
socks4.close()
socks5.close()
allp.close()

# Done!
set_title(f"Bloody Proxy Scraper v{CurrentVersion} | Finished!")
Write.Print(f"[{timenow}] | [!] Successfully Scraped And Saved Proxies!\n\n", Colors.green_to_white, interval=0)
if config["notifications"] == "true" or config["notifications"] == "True":
    toast.show_toast(f"Bloody Proxy Scraper v{CurrentVersion}",
                     "Finished!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
else:
    pass
time.sleep(1)
Write.Print("Thanks for using my tools <3\n", Colors.red_to_yellow, interval=0.1)
Write.Print("Press any key to continue . . .", Colors.green_to_white, interval=0)
pause()
