import json
import re

from bs4 import BeautifulSoup

from dto.item_dto import ItemDTO
from core.logger import logger


class MarketParser:

    def parse(self, html: str):
        logger.info("Parsing Steam Market...")

        # Steam SSR baru
        if "window.SSR.renderContext" in html:
            logger.info("Steam SSR terdeteksi")

            items = self._parse_react_query(html)

            if items:
                return items

            logger.warning("SSR gagal diparse, fallback ke HTML")

        # Steam lama
        return self._parse_html(html)

    #parse versi lama
    def _parse_html(self, html):
        logger.info("Parsing Steam Market HTML...")
        soup = BeautifulSoup(html, "lxml")

        items = []

        cards = soup.select('a[href*="/market/listings/"]')

        logger.info(f"Menemukan {len(cards)} card item")

        for card in cards:

            try:

                item = self._parse_card(card)

                if item:
                    items.append(item)

            except Exception as e:

                logger.warning(e)

        return items

    def _parse_card(self, card):

        market_url = card.get("href", "")

        # Ambil semua span
        spans = [s.get_text(strip=True) for s in card.find_all("span")]

        # Kategori = span pertama
        category = spans[0] if spans else "Unknown"

        # Nama = span kedua
        name = spans[1] if len(spans) > 1 else "Unknown"

        # Quantity
        text = card.get_text(" ", strip=True)

        quantity_match = re.search(
            r"Quantity for sale:\s*([\d,]+)",
            text
        )

        quantity = (
            int(quantity_match.group(1).replace(",", ""))
            if quantity_match else 0
        )

        # Price
        price_match = re.search(
            r"IDR\s*([\d,]+)",
            text
        )

        price = (
            int(price_match.group(1).replace(",", ""))
            if price_match else 0
        )

        # Image
        image_url = ""

        image_div = card.find(style=re.compile(r"--bg-image:url"))

        if image_div:
            style = image_div.get("style", "")

            image_match = re.search(r"url\((.*?)\)", style)

            if image_match:
                image_url = image_match.group(1)

        return ItemDTO(
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            image_url=image_url,
            market_url=market_url
        )

    def _parse_react_query(self, html):
        try:
            match = re.search(
                r'window\.SSR\.renderContext=JSON\.parse\("(.+?)"\);',
                html,
                re.DOTALL
            )

            if not match:
                logger.warning("renderContext tidak ditemukan")
                return []

            # Ambil string JSON
            render_context = match.group(1)

            # Unescape
            render_context = bytes(
                render_context,
                "utf-8"
            ).decode("unicode_escape")

            render_context = json.loads(render_context)

            query_data = json.loads(
                render_context["queryData"]
            )

            return self._parse_queries(query_data)

        except Exception as e:

            logger.exception(e)

            return []

    def _parse_queries(self, query_data):
        items = []

        for query in query_data["queries"]:

            query_key = query.get("queryKey", [])

            if not query_key:
                continue

            if query_key[0] != "market_search":
                continue

            data = query["state"]["data"]
            logger.info(f"Data Keys : {list(data.keys())}")
            pages = data.get("pages", [])

            for page in pages:

                results = page.get("results", [])

                logger.info(
                    f"Jumlah result SSR : {len(results)}"
                )

                for item in results:

                    asset = item.get(
                        "asset_description",
                        {}
                    )

                    name = asset.get(
                        "market_hash_name"
                    )

                    if not name:
                        continue

                    price_text = item.get(
                        "strMinSellSubtotal",
                        ""
                    )

                    price = self._parse_price(
                        price_text
                    )

                    items.append(
                        ItemDTO(
                            name=name,
                            category=asset.get(
                                "type",
                                "Unknown"
                            ),
                            price=price,
                            quantity=item.get(
                                "cSellOrders",
                                0
                            ),
                            image_url=(
                                "https://community."
                                "steamstatic.com/"
                                "economy/image/"
                                +
                                asset.get(
                                    "icon_url",
                                    ""
                                )
                            ),
                            market_url=(
                                "https://steamcommunity.com/"
                                "market/listings/"
                                f"{asset.get('appid')}/"
                                f"{name.replace(' ', '%20')}"
                            )
                        )
                    )

        return items

    def _parse_price(self, text: str) -> int:
        """
        Convert Steam price text to integer IDR.

        Example:
        IDR 12,490       -> 12490
        IDRÂ 2,249       -> 2249
        IDR 1.234.567    -> 1234567
        """

        if not text:
            return 0

        # Normalisasi encoding Steam
        text = (
            text
            .replace("Â", " ")
            .replace(" ", "")
        )

        # Ambil angka saja
        numbers = re.findall(
            r"\d+",
            text
        )

        if not numbers:
            return 0

        return int(
            "".join(numbers)
        )
