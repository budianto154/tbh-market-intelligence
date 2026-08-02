from apscheduler.schedulers.blocking import BlockingScheduler

from core.logger import logger

class MarketScheduler:

    def __init__(
        self,
        market_service
    ):

        self.market_service = market_service
        self.scheduler = BlockingScheduler()

    def sync_job(self):
        logger.info("Scheduler menjalankan market sync...")

        try:
            self.market_service.sync_market()

        except Exception as e:
            logger.exception(e)

    def start(self):
        logger.info("Initial market sync...")

        self.sync_job()
        self.scheduler.add_job(
            self.sync_job,
            trigger="interval",
            minutes=15,
            id="market_sync",
            replace_existing=True
        )

        logger.info( f"Scheduled Jobs: {self.scheduler.get_jobs()}")

        logger.info("Market scheduler aktif (15 menit)")

        self.scheduler.start()