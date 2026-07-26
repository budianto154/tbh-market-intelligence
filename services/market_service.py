from database.item_repository import ItemRepository
from database.market_snapshot_repository import MarketSnapshotRepository

from dto.item_dto import ItemDTO


class MarketService:

    def __init__(
        self,
        scraper,
        parser,
        item_repository,
        snapshot_repository
    ):

        self.scraper = scraper
        self.parser = parser
        self.item_repository = item_repository
        self.snapshot_repository = snapshot_repository

    def save_item(
        self,
        dto: ItemDTO
    ):

        existing = self.item_repository.get_by_market_hash_name(
            dto.name
        )

        if existing:
            return existing, False

        item =  self.item_repository.create(
            steam_name=dto.name,
            market_hash_name=dto.name,
            category=dto.category,
            rarity="Unknown"
        )
        return item, True
    
    def sync_market(self):

        self.scraper.start()

        try:
            html = self.scraper.open_market()
            items = self.parser.parse(html)
            for dto in items:
                item, created = self.save_item(dto)
                print(item.id, item.steam_name, created)

        finally:
            self.scraper.stop()

    