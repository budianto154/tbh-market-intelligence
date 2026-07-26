from database.database import SessionLocal
from database.item_repository import ItemRepository


db = SessionLocal()

repo = ItemRepository(db)

item = repo.create(
    steam_name="Iron Ore",
    market_hash_name="Iron Ore",
    category="Material",
    rarity="Common"
)

print(item.id)
print(item.steam_name)