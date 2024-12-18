import re
import json
import time
import requests
import datetime

from rich import print
from pathlib import Path
from rich.console import Console
from rich.progress import Progress


class ProxyScraper:
    def __init__(self):
        self.version = "2.1.1"
        self.console = Console()
        self.config = self.load_config()
        self.http_urls, self.socks4_urls, self.socks5_urls = self.load_sources()
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

    def load_sources(self):
        try:
            sources_path = Path(__file__).parent / "sources.json"
            with open(sources_path, "r", encoding="utf-8") as sources_file:
                sources = json.load(sources_file)
                return (
                    sources.get("http", []),
                    sources.get("socks4", []),
                    sources.get("socks5", []),
                )
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"[bold red]Error loading sources: {e}")
            print(
                "[yellow]Please ensure sources.json exists and is properly formatted."
            )
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
            self.http_urls, "HTTP(S)", cooldown
        )
        socks4_proxies, socks4_cooldown = self.scrape_proxies(
            self.socks4_urls, "SOCKS4", cooldown
        )
        socks5_proxies, socks5_cooldown = self.scrape_proxies(
            self.socks5_urls, "SOCKS5", cooldown
        )

        # Combine all scraped proxies
        all_proxies = http_proxies + socks4_proxies + socks5_proxies

        return {
            "http": (http_proxies, http_cooldown),
            "socks4": (socks4_proxies, socks4_cooldown),
            "socks5": (socks5_proxies, socks5_cooldown),
            "all": (
                all_proxies,
                False,
            ),  # No need for cooldown flag since these are already scraped
        }

    def write_proxies(self, filename, proxies):
        root_dir = Path(__file__).parent.parent
        scraped_dir = root_dir / "Scraped"
        scraped_dir.mkdir(exist_ok=True)

        now = datetime.datetime.now()
        subfolder = now.strftime("[%Y-%m-%d] [%H-%M-%S]")
        folder_path = scraped_dir / subfolder
        folder_path.mkdir(exist_ok=True)

        # Remove duplicates
        unique_proxies = list(set(proxies))

        # Validate proxies
        # https://stackoverflow.com/questions/18546053/how-to-perfectly-match-a-proxy-with-regex
        valid_proxies = []
        proxy_pattern = re.compile(
            r"^(?:(\w+)(?::(\w+))?@)?((?:\d{1,3})(?:\.\d{1,3}){3})(?::(\d{1,5}))?$"
        )

        for proxy in unique_proxies:
            if proxy_pattern.match(proxy):
                valid_proxies.append(proxy)

        file_path = folder_path / filename
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(valid_proxies))

        print(
            f"[green]Wrote [bold green]{len(valid_proxies)} valid {filename.replace('.txt', '').upper()} proxies[/bold green]"
        )
        print(
            f"[bold white][[bold yellow]-[bold white]] [yellow]Removed [cyan]{len(proxies) - len(unique_proxies)}[/cyan] duplicate proxies"
        )
        print(
            f"[bold white][[bold yellow]-[bold white]] [yellow]Removed [cyan]{len(unique_proxies) - len(valid_proxies)}[/cyan] invalid proxies (not IP:PORT)"
        )

    def save_proxies(self, proxies):
        for proxy_type, (proxy_list, _) in proxies.items():
            self.write_proxies(f"{proxy_type}.txt", proxy_list)
