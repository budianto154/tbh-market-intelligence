from database.item_repository import ItemRepository
from database.market_snapshot_repository import MarketSnapshotRepository


def test_create_snapshot(db_session):

    item_repo = ItemRepository(
        db_session
    )

    snapshot_repo = MarketSnapshotRepository(
        db_session
    )

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

    assert snapshot.id is not None
    assert snapshot.item_id == item.id
    assert snapshot.price == 1200
    assert snapshot.buy_order == 50
    assert snapshot.sell_listing == 45
    assert snapshot.volume == 120

def test_get_history_by_item_id(db_session):

    item_repo = ItemRepository(
        db_session
    )

    snapshot_repo = MarketSnapshotRepository(
        db_session
    )

    item = item_repo.create(
        steam_name="Iron Ore",
        market_hash_name="Iron Ore"
    )

    snapshot_repo.create(
        item_id=item.id,
        price=1200
    )

    snapshot_repo.create(
        item_id=item.id,
        price=1300
    )

    history = snapshot_repo.get_history_by_item_id(
        item.id
    )

    assert len(history) == 2
    assert history[0].price == 1200
    assert history[1].price == 1300