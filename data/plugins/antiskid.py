# For skids
import re
import os
import time
import base64
import psutil
import requests
import subprocess

from pystyle import Write, Colors, Box, Center, Colorate, Anime, Add
from colorama import Fore

skull = """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~ 
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~"""[:-1]

antiSkid_text = """
    ___          __  _      _____ __   _     __
   /   |  ____  / /_(_)    / ___// /__(_)___/ /
  / /| | / __ \/ __/ /_____\__ \/ //_/ / __  / 
 / ___ |/ / / / /_/ /_____/__/ / ,< / / /_/ /  
/_/  |_/_/ /_/\__/_/     /____/_/|_/_/\__,_/   



             Initiating . . .                                                                                               
"""[1:]
antiSkid = Add.Add(skull, antiSkid_text, center=True)

def AntiSkid():
    os.system('cls' if os.name == 'nt' else 'clear')
    Anime.Fade(Center.YCenter(antiSkid), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, time=2)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get Username
    username = os.getenv("UserName")

    # Get Hostname
    hostname = os.getenv("COMPUTERNAME")

    # Get HWID
    hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

    # Get MAC Address
    interface, addrs = next(iter(psutil.net_if_addrs().items()))
    mac = addrs[0].address

    # GET OS
    computer_os = subprocess.run('wmic os get Caption', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().splitlines()[2].strip()

    # Get CPU
    cpu = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True).stdout.strip().split('\n')[2]

    # Get GPU
    gpu = subprocess.run("wmic path win32_VideoController get name", capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip()

    # Get RAM
    ram = str(int(int(subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()[1]) / 1000000000))

    # Get IP and Information
    ip = requests.get('https://api.ipify.org').text
    headers = {
        'authority': 'ipinfo.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'referer': 'https://ipinfo.io/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    r = requests.get(f'https://ipinfo.io/widget/demo/{ip}', headers=headers)
    ip = r.json()['data']['ip']
    city = r.json()['data']['city']
    region = r.json()['data']['region']
    country = r.json()['data']['country']
    timezone = r.json()['data']['timezone']
    address = r.json()['data']['abuse']['address']
    country = r.json()['data']['abuse']['country']

    print(f"""{Fore.RED}[{Fore.RESET}PC Information{Fore.RED}]{Fore.RESET}

{Fore.GREEN}[{Fore.RESET}USERNAME{Fore.GREEN}]{Fore.RESET} {username}
{Fore.GREEN}[{Fore.RESET}DEVICE NAME{Fore.GREEN}]{Fore.RESET} {hostname}
{Fore.GREEN}[{Fore.RESET}OPERATING SYSTEM{Fore.GREEN}]{Fore.RESET} {computer_os}

{Fore.GREEN}[{Fore.RESET}MAC{Fore.GREEN}]{Fore.RESET} {mac}
{Fore.GREEN}[{Fore.RESET}CPU{Fore.GREEN}]{Fore.RESET} {cpu}
{Fore.GREEN}[{Fore.RESET}GPU{Fore.GREEN}]{Fore.RESET} {gpu}
{Fore.GREEN}[{Fore.RESET}RAM{Fore.GREEN}]{Fore.RESET} {ram}GB
{Fore.GREEN}[{Fore.RESET}HWID{Fore.GREEN}]{Fore.RESET} {hwid}

{Fore.RED}[{Fore.RESET}IP Information{Fore.RED}]{Fore.RESET}

{Fore.GREEN}[{Fore.RESET}IP{Fore.GREEN}]{Fore.RESET} {ip}
{Fore.GREEN}[{Fore.RESET}CITY{Fore.GREEN}]{Fore.RESET} {city}
{Fore.GREEN}[{Fore.RESET}REGION{Fore.GREEN}]{Fore.RESET} {region}
{Fore.GREEN}[{Fore.RESET}COUNTRY{Fore.GREEN}]{Fore.RESET} {country}
{Fore.GREEN}[{Fore.RESET}TIMEZONE{Fore.GREEN}]{Fore.RESET} {timezone}
{Fore.GREEN}[{Fore.RESET}ADDRESS{Fore.GREEN}]{Fore.RESET} {address}
""")
    time.sleep(3)
    Write.Print(f"Writing Information . . .\n\n", Colors.purple_to_blue, interval=0.025) 
    data = f"""[ PC Information ]

[ USERNAME ] {username}
[ DEVICE NAME ] {hostname}
[ OPERATING SYSTEM ] {computer_os}
[ MAC ADDRESS ] {mac}
[ CPU ] {cpu}
[ GPU ] {gpu}
[ RAM ] {ram}
[ HWID ] {hwid}

[ IP Information ]

[ IP ] {ip}
[ CITY ] {city}
[ REGION ] {region}
[ COUNTRY ] {country}
[ TIMEZONE ] {timezone}
[ ADDRESS ] {address} (quite innacurate)
"""
    # Encode "data" into ascii then base64 encode it and write it to file
    data_ascii = data.encode('ascii')
    data_encoded = base64.b64encode(data_ascii)
    with open(f"skid-detection_{username}.txt", "wb") as f:
        f.write(data_encoded)
        # This writes the base64 encoded data to the file. If you don't want the encoded data then just remove the # from the line below
        # f.write(data.encode('utf-8'))
        f.close
  
    time.sleep(2)
    Write.Print("Uploading information to database . . .\n", Colors.purple_to_blue, interval=0.025)
    time.sleep(2)
    os.remove(f"skid-detection_{username}.txt")
    Write.Print("Finished uploading information to database\n", Colors.purple_to_blue, interval=0.025)
    Write.Print("Don't skid\n", Colors.purple_to_blue, interval=0.025)
    Write.Print("Press any key to continue . . .", Colors.purple_to_blue, interval=0.025)
    os.system('pause >nul')
    exit
