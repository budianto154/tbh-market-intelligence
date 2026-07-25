from scraper.base_scraper import BaseScraper
from config import STEAM_APP_ID
from core.logger import logger


class SteamScraper(BaseScraper):

    def open_market(self):

        url = f"https://steamcommunity.com/market/search?appid={STEAM_APP_ID}"

        logger.info(f"Membuka {url}")

        self.page.goto(
            url,
            wait_until="commit",
            timeout=60000
        )

        logger.info("Halaman berhasil dimuat")

        self.page.wait_for_timeout(3000)

        return self.page.content()