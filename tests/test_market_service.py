from database.database import SessionLocal
from database.database import init_database
from database.item_repository import ItemRepository

from services.market_service import MarketService

from dto.item_dto import ItemDTO

init_database()

db = SessionLocal()

repo = ItemRepository(db)

service = MarketService(repo)

dto = ItemDTO(
    name="Iron Ore",
    category="Material",
    price=1200,
    quantity=45,
    image_url="https://community.steamstatic.com/image.png",
    market_url="https://steamcommunity.com/market/listings/..."
)

item = service.save_item(dto)

print(item.id)
print(item.steam_name)