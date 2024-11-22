from rich import print
from rich.panel import Panel
from data.utils import Functions
from data.proxyscraper import ProxyScraper
from data.proxychecker import ProxyChecker


def main():
    Functions.clear_screen()
    scraper = ProxyScraper()
    print(Panel(scraper.banner, expand=False))

    proxies = scraper.scrape_all_proxies()
    print("\n[bold green]Finished Scraping Proxies!")

    if scraper.config["check_proxies"]:
        print("\n[bold yellow]Checking proxies...")
        checker = ProxyChecker(scraper.config)
        all_proxies = proxies["all"][0]
        valid_proxies = checker.check_proxies(all_proxies)
        proxies = {
            "http": (valid_proxies, False),
            "socks4": (valid_proxies, False),
            "socks5": (valid_proxies, False),
            "all": (valid_proxies, False),
        }
        print(
            f"[green]Found {len(valid_proxies)} valid proxies out of {len(all_proxies)}"
        )

    Functions.clear_screen()

    if any(cooldown for _, cooldown in proxies.values()):
        print("[green]Cooldown was applied during scraping.[/green]")

    scraper.save_proxies(proxies)

    print("\n[bold green]Successfully Scraped and Saved Proxies!")
    print("[cyan]Proxies are saved as http.txt, socks4.txt, socks5.txt, and all.txt")
    print("[cyan]in the 'Scraped/[YYYY-MM-DD] [HH-MM-SS]' folder.")
    scraper.console.input("[bold cyan]Press ENTER to exit...[/bold cyan]")


if __name__ == "__main__":
    Functions.clean_up_cache()
    main()
