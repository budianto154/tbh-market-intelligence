from unittest.mock import Mock

from services.market_service import MarketService

from database.item_repository import ItemRepository
from database.market_snapshot_repository import MarketSnapshotRepository

from dto.item_dto import ItemDTO


def create_service(db_session):

    scraper = Mock()
    parser = Mock()

    item_repository = ItemRepository(
        db_session
    )

    snapshot_repository = MarketSnapshotRepository(
        db_session
    )

    service = MarketService(
        scraper=scraper,
        parser=parser,
        item_repository=item_repository,
        snapshot_repository=snapshot_repository
    )
    return service, scraper, parser, snapshot_repository

def test_sync_market_smart_snapshot(db_session):
    service, scraper, parser, snapshot_repo = create_service(
        db_session
    )

    item = ItemDTO(
        name="Empire Coin",
        category="Offering Material",
        price=12000,
        quantity=50,
        image_url="",
        market_url=""
    )

    parser.parse.return_value = [item]

    scraper.open_market.return_value = "<html></html>"

    # Sync pertama
    service.sync_market()

    history = snapshot_repo.get_history_by_item_id(1)

    assert len(history) == 1
    assert history[0].price == 12000

    # Sync kedua (harga sama)
    service.sync_market()

    history = snapshot_repo.get_history_by_item_id(1)

    assert len(history) == 1

    # Sync ketiga (harga berubah)
    item.price = 13000

    service.sync_market()

    history = snapshot_repo.get_history_by_item_id(
        1
    )

    assert len(history) == 2
    assert history[1].price == 13000