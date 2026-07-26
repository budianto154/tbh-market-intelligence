from dataclasses import dataclass


@dataclass
class ItemDTO:
    name: str
    category: str

    price: int
    quantity: int

    image_url: str
    market_url: str