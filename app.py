from database.database import init_database
from scraper.steam_scraper import SteamScraper
from parser.market_parser import MarketParser


def main():

    print("=" * 40)
    print("TBH Market Intelligence")
    print("=" * 40)

    init_database()

    scraper = SteamScraper()
    parser = MarketParser()

    try:
        scraper.start()

        html = scraper.open_market()

        print("Scraping selesai")

        items = parser.parse(html)

        print(f"Jumlah item : {len(items)}")

        for item in items[:10]:
            print(item)

    finally:
        scraper.stop()


if __name__ == "__main__":
    main()