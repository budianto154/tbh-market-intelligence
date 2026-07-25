from sqlalchemy.orm import Session

from database.models import Item


class ItemRepository:

    def __init__(self, db: Session):
        self.db = db

    #mencari apakah item udah ada
    def get_by_market_hash_name(self, market_hash_name: str):

        return (
            self.db.query(Item)
            .filter(Item.market_hash_name == market_hash_name)
            .first()
        )

    #menyimpan item baru
    def create(
        self,
        steam_name: str,
        market_hash_name: str,
        category: str = "Unknown",
        rarity: str = "Unknown"
    ):

        item = Item(
            steam_name=steam_name,
            market_hash_name=market_hash_name,
            category=category,
            rarity=rarity
        )

        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item

    #mengambil seluruh item
    def get_all(self):

        return self.db.query(Item).all()