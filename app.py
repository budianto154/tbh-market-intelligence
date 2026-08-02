from database.database import SessionLocal, init_database

from database.item_repository import ItemRepository
from database.market_snapshot_repository import MarketSnapshotRepository

from scraper.steam_scraper import SteamScraper
from parser.market_parser import MarketParser

from services.market_service import MarketService

from scheduler.market_scheduler import MarketScheduler


def main():

    print("Starting TBH Market Intelligence...")

    # Database
    init_database()
    db = SessionLocal()

    # Core components
    scraper = SteamScraper()
    parser = MarketParser()

    # Repository
    item_repository = ItemRepository(db)

    snapshot_repository = MarketSnapshotRepository(db)

    # Service
    market_service = MarketService(
        scraper=scraper,
        parser=parser,
        item_repository=item_repository,
        snapshot_repository=snapshot_repository
    )

    # Scheduler
    scheduler = MarketScheduler(market_service)
    scheduler.start()

if __name__ == "__main__":
    main()