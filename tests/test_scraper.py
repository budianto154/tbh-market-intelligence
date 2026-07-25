from scraper.steam_scraper import SteamScraper

scraper = SteamScraper()

try:
    scraper.start()

    html = scraper.open_market()

    with open("market.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML berhasil disimpan!")

finally:
    scraper.stop()