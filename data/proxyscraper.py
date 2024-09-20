import os
import re
import json
import time
import requests
import datetime
import concurrent.futures

from rich import print
from pathlib import Path
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.progress import Progress
from data.sources import http_urls, socks4_urls, socks5_urls, all_urls
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn


class Functions:
    @staticmethod
    def clean_up_cache():
        for p in Path(".").rglob("*.py[co]"):
            p.unlink()
        for p in Path(".").rglob("__pycache__"):
            p.rmdir()


class ProxyScraper:
    def __init__(self):
        self.version = "2.1.0"
        self.console = Console()
        self.config = self.load_config()
        self.banner = self.create_banner()

    def load_config(self):
        try:
            config_path = Path(__file__).parent.parent / "config.json"
            with open(config_path, "r", encoding="utf-8") as config_file:
                return json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"[bold red]Error loading configuration: {e}")
            print("[yellow]Please ensure config.json exists and is properly formatted.")
            exit(1)

    def create_banner(self):
        return f"""
[bold purple]██████╗ ██████╗ ███████╗[/bold purple]
[bold purple]██╔══██╗██╔══██╗██╔════╝[/bold purple]
[bold purple]██████╔╝██████╔╝███████╗[/bold purple]
[bold purple]██╔══██╗██╔═══╝ ╚════██║[/bold purple]
[bold purple]██████╔╝██║     ███████║[/bold purple]
[bold purple]╚═════╝ ╚═╝     ╚══════╝[/bold purple] v{self.version}
"""

    def get_cooldown(self):
        optional_cooldown = Prompt.ask(
            "[bold cyan]Do you want a cooldown between each scrape? (y/n)"
        )
        if optional_cooldown.lower() == "y":
            cooldown_input = Prompt.ask(
                "[bold cyan]How much do you want the cooldown to be? (in seconds)"
            )
            cooldown = int(cooldown_input.replace(".", ""))
            print(f"[green]Cooldown set to: {cooldown} seconds")
            return cooldown
        return 0

    def scrape_proxies(self, urls, proxy_type, cooldown=0):
        proxies = []
        cooldown_used = False
        with Progress() as progress:
            task = progress.add_task(
                f"[cyan]Scraping {proxy_type} proxies...", total=len(urls)
            )
            for url in urls:
                try:
                    response = requests.get(url, timeout=10)
                    proxies.extend(response.text.strip().split("\n"))
                    progress.update(task, advance=1)
                    if cooldown > 0:
                        time.sleep(cooldown)
                        cooldown_used = True
                except requests.RequestException:
                    pass
        return proxies, cooldown_used

    def scrape_all_proxies(self):
        print("\n[bold yellow]Scraping Proxies...")
        cooldown = self.config["cooldown_per_scrape"]
        http_proxies, http_cooldown = self.scrape_proxies(
            http_urls, "HTTP(S)", cooldown
        )
        socks4_proxies, socks4_cooldown = self.scrape_proxies(
            socks4_urls, "SOCKS4", cooldown
        )
        socks5_proxies, socks5_cooldown = self.scrape_proxies(
            socks5_urls, "SOCKS5", cooldown
        )
        all_proxies, all_cooldown = self.scrape_proxies(all_urls, "ALL", cooldown)

        return {
            "http": (http_proxies, http_cooldown),
            "socks4": (socks4_proxies, socks4_cooldown),
            "socks5": (socks5_proxies, socks5_cooldown),
            "all": (all_proxies, all_cooldown),
        }

    def write_proxies(self, filename, proxies):
        root_dir = Path(__file__).parent.parent
        scraped_dir = root_dir / "Scraped"
        scraped_dir.mkdir(exist_ok=True)

        now = datetime.datetime.now()
        subfolder = now.strftime("[%Y-%m-%d] [%H-%M]")
        folder_path = scraped_dir / subfolder
        folder_path.mkdir(exist_ok=True)

        # Remove duplicates
        unique_proxies = list(set(proxies))

        # Validate proxies
        valid_proxies = []
        # https://stackoverflow.com/questions/18546053/how-to-perfectly-match-a-proxy-with-regex
        proxy_pattern = re.compile(
            r"^(?:(\w+)(?::(\w+))?@)?((?:\d{1,3})(?:\.\d{1,3}){3})(?::(\d{1,5}))?$"
        )

        for proxy in unique_proxies:
            if proxy_pattern.match(proxy):
                valid_proxies.append(proxy)

        file_path = folder_path / filename
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(valid_proxies))

        print(f"[green]Wrote {len(valid_proxies)} valid proxies to {filename}")
        print(f"[yellow]Removed {len(proxies) - len(unique_proxies)} duplicate proxies")
        print(
            f"[yellow]Removed {len(unique_proxies) - len(valid_proxies)} invalid proxies (not IP:PORT)"
        )

    def save_proxies(self, proxies):
        for proxy_type, (proxy_list, _) in proxies.items():
            self.write_proxies(f"{proxy_type}.txt", proxy_list)

    def check_proxy(self, proxy):
        try:
            response = requests.get(
                "https://ipv4.games/claim?name=noobtoolzz",
                proxies={"http": proxy, "https": proxy},
                timeout=10,
            )
            return proxy if response.status_code == 200 else None
        except:
            return None

    def check_proxies(self, proxies):
        threads = self.config["proxy_checking_threads"]
        valid_proxies = []
        total_proxies = len(proxies)

        progress = Progress(
            SpinnerColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            BarColumn(),
            TextColumn("[bold blue]{task.completed}/{task.total} checked"),
            TextColumn("[green]{task.fields[valid]} valid"),
        )

        task = progress.add_task("Checking", total=total_proxies, valid=0)

        with Live(progress, refresh_per_second=10) as live:
            with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                future_to_proxy = {
                    executor.submit(self.check_proxy, proxy): proxy for proxy in proxies
                }
                for future in concurrent.futures.as_completed(future_to_proxy):
                    result = future.result()
                    if result:
                        valid_proxies.append(result)
                    progress.update(task, advance=1, valid=len(valid_proxies))

        return valid_proxies

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(Panel(self.banner, expand=False))

        proxies = self.scrape_all_proxies()
        print("\n[bold green]Finished Scraping Proxies!")

        if self.config["check_proxies"]:
            print("\n[bold yellow]Checking proxies...")
            all_proxies = proxies["all"][0]
            valid_proxies = self.check_proxies(all_proxies)
            proxies = {
                "http": (valid_proxies, False),
                "socks4": (valid_proxies, False),
                "socks5": (valid_proxies, False),
                "all": (valid_proxies, False),
            }
            print(
                f"[green]Found {len(valid_proxies)} valid proxies out of {len(all_proxies)}"
            )

        os.system("cls" if os.name == "nt" else "clear")

        if any(cooldown for _, cooldown in proxies.values()):
            print("[yellow]Cooldown was applied during scraping.[/yellow]")
        else:
            print("[green]No cooldown was applied during scraping.[/green]")

        self.save_proxies(proxies)

        print("\n[bold green]Successfully Scraped and Saved Proxies!")
        print(
            "[cyan]Proxies are saved as http.txt, socks4.txt, socks5.txt, and all.txt"
        )
        print("[cyan]in the 'Scraped/[YYYY-MM-DD] [HH-MM]' folder.")
        self.console.input("[bold cyan]Press Enter to exit...[/bold cyan]")
