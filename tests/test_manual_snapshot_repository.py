from database.database import SessionLocal
from database.database import init_database

from database.item_repository import ItemRepository
from database.market_snapshot_repository import MarketSnapshotRepository

init_database()

db = SessionLocal()

item_repo = ItemRepository(db)
snapshot_repo = MarketSnapshotRepository(db)

item = item_repo.get_by_market_hash_name("Iron Ore")

if item is None:

    item = item_repo.create(
        steam_name="Iron Ore",
        market_hash_name="Iron Ore",
        category="Material",
        rarity="Common"
    )

snapshot = snapshot_repo.create(
    item_id=item.id,
    price=1200,
    buy_order=50,
    sell_listing=45,
    volume=120
)

print(snapshot.id)
print(snapshot.price)
print(snapshot.item_id)