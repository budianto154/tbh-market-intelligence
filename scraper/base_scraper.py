from playwright.sync_api import sync_playwright

from config import HEADLESS
from core.logger import logger


class BaseScraper:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):

        logger.info("Menjalankan Playwright...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=HEADLESS,
            slow_mo=300
        )

        self.context = self.browser.new_context(
            viewport={"width": 1600, "height": 900},
            locale="en-US",
        )

        self.page = self.context.new_page()

    def stop(self):

        logger.info("Menutup browser...")

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()