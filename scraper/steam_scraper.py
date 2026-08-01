from scraper.base_scraper import BaseScraper
from config import STEAM_APP_ID
from core.logger import logger


class SteamScraper(BaseScraper):

    def __init__(self):
        super().__init__()

    def open_market(self):
        print("SteamScraper berjalan")

        url = f"https://steamcommunity.com/market/search?appid={STEAM_APP_ID}"

        logger.info(f"Membuka {url}")


        # Capture network response
        def handle_response(response):

            url = response.url
            if (
                "steamcommunity.com" in url
                or "steamstatic.com" in url
            ):

                logger.info(
                    f"REQUEST : {url}"
                )

            #if "steamcommunity.com/market" in response.url:

                #logger.info("========== STEAM RESPONSE ==========")
                #logger.info(f"URL : {response.url}")
                #logger.info(f"METHOD : {response.request.method}")
                #logger.info(f"STATUS : {response.status}")

                #content_type = response.headers.get(
                #    "content-type",
                #    ""
                #)

                #logger.info(f"TYPE : {content_type}")

                #if "application/json" in content_type:

                #    try:
                #        data = response.json()
                #        logger.info(data)

                #    except Exception as e:
                #        logger.error(
                #            f"Gagal membaca JSON: {e}"
                #        )


        self.page.on(
            "response",
            handle_response
        )


        self.page.goto(
            url,
            wait_until="networkidle",
            timeout=60000
        )

        logger.info("Halaman berhasil dimuat")

        self.page.wait_for_timeout(15000)

        title = self.page.title()

        logger.info(
            f"TITLE : {title}"
        )


        content = self.page.content()

        logger.info(
            f"HTML SIZE : {len(content)}"
        )

        keywords = [
            "Iron Ore",
            "Empire 50th Anniversary Coin",
            "market_listing",
            "listingid",
            "market_hash_name"
        ]

        for keyword in keywords:
            if keyword in content:
                logger.info(
                    f"FOUND : {keyword}"
                )
            else:
                logger.info(
                    f"NOT FOUND : {keyword}"
                )

            index = content.find("market_hash_name")
            logger.info(
                f"market_hash_name position : {index}"
            )

            if index != -1:
                logger.info(
                    content[index-500:index+500]
                )

            with open(
                "debug_market.html",
                "w",
                encoding="utf-8"
            ) as f:
                f.write(content)  

        return self.page.content()