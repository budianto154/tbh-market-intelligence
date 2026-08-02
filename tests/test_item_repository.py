from database.item_repository import ItemRepository


def test_create_item(db_session):

    repo = ItemRepository(
        db_session
    )

    item = repo.create(
        steam_name="Empire Coin",
        market_hash_name="Empire Coin",
        category="Offering Material",
        rarity="Unknown"
    )

    assert item.id is not None

    assert item.steam_name == "Empire Coin"

    assert item.category == "Offering Material"

def test_get_by_market_hash_name(db_session):

    repo = ItemRepository(
        db_session
    )

    repo.create(
        steam_name="Empire Coin",
        market_hash_name="Empire Coin"
    )

    item = repo.get_by_market_hash_name(
        "Empire Coin"
    )

    assert item is not None

    assert item.market_hash_name == "Empire Coin"