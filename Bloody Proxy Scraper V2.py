import os, time, requests, pystyle, random, datetime

from pystyle import Write, Colors, Colorate, Center
from console.utils import set_title
from colorama import Fore

from data.sources import http_urls, socks4_urls, socks5_urls, all_urls
from data.plugins.common import MainUpdater, CommonUpdater, SkidUpdater, VersionFileRemover
from data.plugins.antiskid import AntiSkid
from win10toast import ToastNotifier
toast = ToastNotifier()

# Check if version.txt exists. If it does, delete it.
VersionFileRemover()

# Check for updates to main file, and both files in data/plugins
print(f"{Fore.GREEN}[{Fore.RESET}INFO{Fore.GREEN}]{Fore.RESET} Checking for updates . . .")
MainUpdater()
time.sleep(0.5)
CommonUpdater()
time.sleep(0.5)
SkidUpdater()

# Anti-Skid
__author__ = 'NoNoobz'

if __author__ != '\u004E\u006F\u004E\u006F\u006F\u0062\u007A':
    AntiSkid()

def cls():
    os.system('cls')

def pause():
    os.system('pause >nul')

h_h2 = ["Halal", "Haram"]
now = datetime.datetime.now()   

cls()
# os.system('mode 85, 25')
banner = '''
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗     
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝     
██████╔╝██║     ██║   ██║██║   ██║██║  ██║ ╚████╔╝      
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║  ╚██╔╝       
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝   ██║        
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝        
                                                        
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗              
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝              
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝               
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝                
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║                 
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝                 
                                                        
███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
A simple proxy scraper made by Bloody.
github/BloodyToolzz
'''
toast.show_toast("Bloody Proxy Scraper V2",
                     "Started to scrape proxies.",
                     icon_path="data\icons\logo.ico",
                     duration=2)
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
Write.Print("This program is: ", Colors.purple_to_blue, interval=0)
Write.Print(f"{random.choice(h_h2)}\n", Colors.green_to_white, interval=0)
Write.Print("Started at: " + now.strftime("%Y/%m/%d %H:%M:%S\n"), Colors.purple_to_blue , interval=0)
time.sleep(1)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Scraping Proxies . . .")
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
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped HTTP Proxies from {url}!")
        Write.Print(f"\n[?] Scraped HTTP Proxies from {url}\n", Colors.green_to_blue, interval=0)
        http_proxies.extend(scrape_http.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped HTTP Proxies!")
Write.Print("[?] Scraped HTTP(S) Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
toast.show_toast("Bloody Proxy Scraper V2",
                     "Scraped HTTP(S) Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
time.sleep(1)

# Scrape SOCKS4 proxies from their sources
socks4_proxies = []
for url in socks4_urls:
    try:
        scrape_socks4 = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS4 Proxies from {url}!")
        Write.Print(f"\n[?] Scraped SOCKS4 Proxies from {url}\n", Colors.green_to_blue, interval=0)
        socks4_proxies.extend(scrape_socks4.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS4 Proxies!")
Write.Print("[?] Scraped SOCKS4 Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
toast.show_toast("Bloody Proxy Scraper V2",
                     "Scraped SOCKS4 Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
time.sleep(1)

# Scrape SOCKS5 proxies from their sources
socks5_proxies = []
for url in socks5_urls:
    try:
        scrape_socks5 = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS5 Proxies from {url}!")
        Write.Print(f"\n[?] Scraped SOCKS5 Proxies from {url}\n", Colors.green_to_blue, interval=0)
        socks5_proxies.extend(scrape_socks5.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS5 Proxies!")
Write.Print("[?] Scraped SOCKS5 Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
toast.show_toast("Bloody Proxy Scraper V2",
                     "Scraped SOCKS5 Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
time.sleep(1)

# Scrape ALL proxies from their sources
all_proxies = []
for url in all_urls:
    try:
        scrape_all = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped ALL Proxies from {url}!")
        Write.Print(f"\n[?] Scraped ALL Proxies from {url}\n", Colors.green_to_blue, interval=0)
        all_proxies.extend(scrape_all.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped ALL Proxies!")
Write.Print("[?] Scraped ALL Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
toast.show_toast("Bloody Proxy Scraper V2",
                     "Scraped ALL Proxies!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
time.sleep(1)

set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Finished Scraping Proxies!")
Write.Print(f"[!] Finished Scraping Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Writing Proxies . . .")
Write.Print("[?] Writing Proxies In Files . . .\n\n", Colors.red_to_yellow, interval=0)
toast.show_toast("Bloody Proxy Scraper V2",
                     "Writing Proxies...",
                     icon_path="data\icons\logo.ico",
                     duration=1)
time.sleep(1)

# Writing Proxies In Their Files

# Write HTTP(s) proxies to file
with open('proxies-http.txt','wb') as http:
    for proxy in http_proxies:
        http.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote HTTP Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

# Write SOCKS4 proxies to file
with open('proxies-socks4.txt','wb') as socks4:
    for proxy in socks4_proxies:
        socks4.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote SOCKS4 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

# Write SOCKS5 proxies to file
with open('proxies-socks5.txt','wb') as socks5:
    for proxy in socks5_proxies:
        socks5.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote SOCKS5 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

# Write SOCKS4 proxies to file
with open('proxies-all.txt','wb') as allp:
    for proxy in all_proxies:
        allp.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote ALL Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(0.3)

set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Wrote Proxies!")
Write.Print("[!] Finished Writing Proxies In Files!\n", Colors.green_to_white, interval=0)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(0.5)

set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Closing Files . . .")
Write.Print("[?] Closing Files . . .\n", Colors.red_to_yellow, interval=0)
time.sleep(0.5)

# Closing Files
http.close()
socks4.close()
socks5.close()
allp.close()

# Done!
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Finished!")
Write.Print("[!] Successfully Scraped And Saved Proxies!\n\n", Colors.green_to_white, interval=0)
toast.show_toast("Bloody Proxy Scraper V2",
                     "Finished!",
                     icon_path="data\icons\logo.ico",
                     duration=1)
time.sleep(1)
Write.Print("Thanks for using my tools <3\n", Colors.red_to_yellow, interval=0.1)
Write.Print("Press any key to continue . . .", Colors.green_to_white, interval=0)
pause()
