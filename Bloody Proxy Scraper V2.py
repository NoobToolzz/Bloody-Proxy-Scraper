import os, time, requests, pystyle, random, datetime

from pystyle import Write, Colors, Colorate, Center
from console.utils import set_title

def cls():
    os.system('cls')

def pause():
    os.system('pause >nul')

h_h2 = ["Halal", "Haram"]

now = datetime.datetime.now()

# Proxy Sources
http_urls = [
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxyscan.io/download?type=http",
    "https://www.proxyscan.io/download?type=https",
    "https://api.openproxylist.xyz/http.txt"
]

socks4_urls = [
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://www.proxyscan.io/download?type=socks4",
    "https://api.openproxylist.xyz/socks4.txt"
]

socks5_urls = [
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://www.proxyscan.io/download?type=socks5",
    "https://api.openproxylist.xyz/socks5.txt"
]

all_urls = [
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxyscan.io/download?type=http",
    "https://www.proxyscan.io/download?type=https",
    "https://api.openproxylist.xyz/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://www.proxyscan.io/download?type=socks4",
    "https://api.openproxylist.xyz/socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://www.proxyscan.io/download?type=socks5",
    "https://api.openproxylist.xyz/socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
    "http://hack-hack.chat.ru/proxy/allproxy.txt",
    "http://hack-hack.chat.ru/proxy/p1.txt",
    "http://hack-hack.chat.ru/proxy/p2.txt",
    "http://hack-hack.chat.ru/proxy/p3.txt",
    "http://hack-hack.chat.ru/proxy/p4.txt",
    "http://olaf4snow.com/public/proxy.txt",
    "http://alexa.lr2b.com/proxylist.txt",
    "http://inav.chat.ru/ftp/proxy.txt"
]

    

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
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
Write.Print("This program is: ", Colors.purple_to_blue, interval=0)
Write.Print(f"{random.choice(h_h2)}\n", Colors.green_to_white, interval=0)
Write.Print("Started at: " + now.strftime("%Y/%m/%d %H:%M:%S\n"), Colors.purple_to_blue , interval=0)
time.sleep(1)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Scraping Proxies . . .")
Write.Print("[?] Scraping Proxies . . .\n", Colors.red_to_yellow, interval=0)

# Opening/Adding proxy files
http = open('proxies-http.txt','wb')
socks4 = open('proxies-socks4.txt','wb')
socks5 = open('proxies-socks5.txt','wb')
allp = open('proxies-all.txt','wb')
# scraped_sites = 0

# Scrape HTTP(s) proxies from their sources 
http_proxies = []
for url in http_urls:
    try:
        scrape_http = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped HTTP Proxies from {url}!")
        Write.Print(f"\n[?] Scraped HTTP Proxies from {url}!\n", Colors.green_to_blue, interval=0)
        http_proxies.extend(scrape_http.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped HTTP Proxies!")
Write.Print("[?] Scraped HTTP Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)

# Scrape SOCKS4 proxies from their sources
socks4_proxies = []
for url in socks4_urls:
    try:
        scrape_socks4 = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS4 Proxies from {url}!")
        Write.Print(f"\n[?] Scraped SOCKS4 Proxies from {url}!\n", Colors.green_to_blue, interval=0)
        socks4_proxies.extend(scrape_socks4.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS4 Proxies!")
Write.Print("[?] Scraped SOCKS4 Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)

# Scrape SOCKS5 proxies from their sources
socks5_proxies = []
for url in socks5_urls:
    try:
        scrape_socks5 = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS5 Proxies from {url}!")
        Write.Print(f"\n[?] Scraped SOCKS5 Proxies from {url}!\n", Colors.green_to_blue, interval=0)
        socks5_proxies.extend(scrape_socks5.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS5 Proxies!")
Write.Print("[?] Scraped SOCKS5 Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)

# Scrape ALL proxies from their sources
all_proxies = []
for url in all_urls:
    try:
        scrape_all = requests.get(url)
        # Process the scraped proxies here
        set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped ALL Proxies from {url}!")
        Write.Print(f"\n[?] Scraped ALL Proxies from {url}!\n", Colors.green_to_blue, interval=0)
        all_proxies.extend(scrape_all.text.strip().split('\n'))
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        Write.Print(f"[!] Error scraping proxies from {url}: {e}\n", Colors.red_to_yellow, interval=0)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped ALL Proxies!")
Write.Print("[?] Scraped ALL Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)

set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Finished Scraping Proxies!")
Write.Print(f"[!] Finished Scraping Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Writing Proxies . . .")
Write.Print("[?] Writing Proxies In Files . . .\n\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Writing Proxies In Their Files

# Write HTTP(s) proxies to file
for proxy in http_proxies:
    http.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote HTTP Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Write SOCKS4 proxies to file
for proxy in socks4_proxies:
    socks4.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote SOCKS4 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Write SOCKS5 proxies to file
for proxy in socks5_proxies:
    socks5.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote SOCKS5 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Write SOCKS4 proxies to file
for proxy in all_proxies:
    allp.write(proxy.encode('utf-8') + b'\n')
Write.Print("[?] Wrote ALL Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Wrote Proxies!")
Write.Print("[!] Finished Writing Proxies In Files!\n", Colors.green_to_white, interval=0)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)

set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Closing Files . . .")
Write.Print("[?] Closing Files . . .\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Closing Files
http.close()
socks4.close()
socks5.close()
allp.close()

# Done!
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Finished!")
Write.Print("[!] Successfully Scraped And Saved Proxies!\n\n", Colors.green_to_white, interval=0)
time.sleep(1)
Write.Print("Thanks for using my tools <3\n", Colors.red_to_yellow, interval=0.1)
Write.Print("Press any key to continue . . .", Colors.green_to_white, interval=0)
pause()
