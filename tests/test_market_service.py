from database.database import SessionLocal

from database.item_repository import ItemRepository
from database.market_snapshot_repository import MarketSnapshotRepository

from scraper.steam_scraper import SteamScraper
from parser.market_parser import MarketParser

from services.market_service import MarketService


db = SessionLocal()

scraper = SteamScraper()
parser = MarketParser()

item_repo = ItemRepository(db)
snapshot_repo = MarketSnapshotRepository(db)

service = MarketService(
    scraper=scraper,
    parser=parser,
    item_repository=item_repo,
    snapshot_repository=snapshot_repo
)

service.sync_market()