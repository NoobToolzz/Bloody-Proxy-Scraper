import os, time, requests, pystyle, random, datetime

from pystyle import *
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
os.system('mode 85, 25')
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
scraped_sites = 0

# Scrape HTTP(s) proxies from their sources 
scrape_http = requests.get(http_urls)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped HTTP Proxies!")
Write.Print("\n[?] Scraped HTTP Proxies!\n", Colors.red_to_yellow, interval=0)

# Scrape SOCKS4 proxies from their sources
scrape_socks4 = requests.get(socks4_urls)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS4 Proxies!")
Write.Print("[?] Scraped SOCKS4 Proxies!\n", Colors.red_to_yellow, interval=0)

# Scrape SOCKS5 proxies from their sources
scrape_socks5 = requests.get(socks5_urls)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped SOCKS5 Proxies!")
Write.Print("[?] Scraped SOCKS5 Proxies!\n", Colors.red_to_yellow, interval=0)

# All Proxies Sources
scrape_all = requests.get(all_urls)
set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped ALL Proxies!")
Write.Print("[?] Scraped ALL Proxies!\n", Colors.red_to_yellow, interval=0)

set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Finished Scraping Proxies!")
Write.Print(f"[!] Finished Scraping Proxies!\n", Colors.green_to_white, interval=0)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Writing Proxies . . .")
Write.Print("[?] Writing Proxies In Files . . .\n\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Writing Proxies In Their Files
# Writing HTTP Proxies
http.write(scrape_socks4.content)
Write.Print("[?] Wrote HTTP Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Writing SOCKS4 Proxies
socks4.write(scrape_socks4.content)
Write.Print("[?] Wrote SOCKS4 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Writing SOCKS5 Proxies
socks5.write(scrape_socks5.content)
Write.Print("[?] Wrote SOCKS5 Proxies!\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Writing All Proxies 
allp.write(scrape_all.content)
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
