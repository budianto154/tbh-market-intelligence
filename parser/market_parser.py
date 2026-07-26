import re
from bs4 import BeautifulSoup

from dto.item_dto import ItemDTO
from core.logger import logger


class MarketParser:

    def parse(self, html: str):
        print("Parsing Steam Market...")

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
                logger.warning(f"Gagal parse card: {e}")

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