from data.proxyscraper import ProxyScraper, Functions


def main():
    scraper = ProxyScraper()
    scraper.run()


if __name__ == "__main__":
    Functions.clean_up_cache()
    main()
