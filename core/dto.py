from dataclasses import dataclass


@dataclass
class MarketItemDTO:
    #Data Transfer Object

    steam_name: str

    market_hash_name: str

    category: str

    rarity: str

    price: float = 0

    buy_order: int = 0

    sell_listing: int = 0

    volume: int = 0