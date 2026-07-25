from core.dto import MarketItemDTO


item = MarketItemDTO(
    steam_name="Iron Ore",
    market_hash_name="Iron Ore",
    category="Material",
    rarity="Common",
    price=150
)

print(item)