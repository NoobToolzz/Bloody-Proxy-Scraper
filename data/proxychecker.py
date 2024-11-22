import requests
import concurrent.futures
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn


class ProxyChecker:
    def __init__(self, config):
        self.config = config

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
