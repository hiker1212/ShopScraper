from src.shopscraper.scrapers.scraper import mediamarkt_scrap
from src.shopscraper.write_to_csv.write_to_csv import write_to_csv
import csv

if __name__ == "__main__":
    devices = mediamarkt_scrap()
    for device in devices:
        print(str(device))

    write_to_csv(devices)

