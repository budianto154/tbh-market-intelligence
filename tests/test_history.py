from database.database import SessionLocal

from database.item_repository import ItemRepository
from database.market_snapshot_repository import MarketSnapshotRepository

from services.market_service import MarketService


db = SessionLocal()

item_repo = ItemRepository(db)
snapshot_repo = MarketSnapshotRepository(db)

service = MarketService(
    scraper=None,
    parser=None,
    item_repository=item_repo,
    snapshot_repository=snapshot_repo
)

item, history = service.get_price_history(
    #"Empire 50th Anniversary Coin"
    "Iron Ore"
)

print("=" * 60)

if item is None:

    print("Item tidak ditemukan.")

else:

    print(f"Item     : {item.steam_name}")
    print(f"Category : {item.category}")
    print(f"History  : {len(history)} Snapshot")
    print("=" * 60)

    for snapshot in history:

        print(
            snapshot.updated_at,
            snapshot.price,
            snapshot.sell_listing
        )