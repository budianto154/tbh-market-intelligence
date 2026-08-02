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
    
    def sync_market(self):
        self.scraper.start()
        try:
            html = self.scraper.open_market()
            items = self.parser.parse(html)

            if not items:
                print("Tidak ada item yang berhasil diparse.")
                return

            self._save_market(items)

        finally:

            self.scraper.stop()

    def save_item(
            self,
            dto: ItemDTO
        ):
    
            existing = self.item_repository.get_by_market_hash_name(
                dto.name
            )
    
            if existing is not None:
                return existing, False
    
            created = self.item_repository.create(
                steam_name=dto.name,
                market_hash_name=dto.name,
                category=dto.category,
                rarity="Unknown"
            )
            return created, True

    def get_price_history(
            self,
            steam_name: str
        ):
    
            item = self.item_repository.get_by_steam_name(
                steam_name
            )
    
            if item is None:
                return None, []
    
            history = self.snapshot_repository.get_history_by_item_id(
                item.id
            )
    
            return item, history

    def _save_market(
        self,
        items: list[ItemDTO]
    ):

        new_item = 0
        existing_item = 0

        for dto in items:

            item, created = self.save_item(dto)

            if created:
                new_item += 1
            else:
                existing_item += 1

            self._save_snapshot(
                item.id,
                dto
            )

        self._print_summary(
            len(items),
            new_item,
            existing_item
        )

    def _save_snapshot(
        self,
        item_id: int,
        dto: ItemDTO
    ):

        self.snapshot_repository.create(
            item_id=item_id,
            price=dto.price,
            sell_listing=dto.quantity
        )

    def _print_summary(
        self,
        total_item: int,
        new_item: int,
        existing_item: int
    ):

        print("=" * 60)
        print("Steam Market Synchronization")
        print("=" * 60)
        print(f"Total Item      : {total_item}")
        print(f"Item Baru       : {new_item}")
        print(f"Item Existing   : {existing_item}")
        print(f"Snapshot        : {total_item}")
        print("=" * 60)
        