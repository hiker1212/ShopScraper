from src.shopscraper.scrapers.scraper import mediamarkt_scrap

if __name__ == "__main__":
    devices = mediamarkt_scrap()
    for device in devices:
        print(str(device))