from database.item_repository import ItemRepository

from dto.item_dto import ItemDTO


class MarketService:

    def __init__(
        self,
        item_repository: ItemRepository
    ):

        self.item_repository = item_repository

    def save_item(
        self,
        dto: ItemDTO
    ):

        existing = self.item_repository.get_by_market_hash_name(
            dto.name
        )

        if existing:

            return existing

        return self.item_repository.create(
            steam_name=dto.name,
            market_hash_name=dto.name,
            category=dto.category,
            rarity="Unknown"
        )