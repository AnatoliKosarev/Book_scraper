import logging
import re
from bs4 import BeautifulSoup

from milestone_3_Book_scraper.locators.book_page_locators import BookPageLocators
from milestone_3_Book_scraper.parsers.book import BookParser

logger = logging.getLogger("scraping.book_page")

class BookPage:

    def __init__(self, page_content):
        logger.debug("Parsing page content with BeautifulSoup HTML parser.")
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books(self):
        locator = BookPageLocators.BOOK
        logger.debug(f"Finding all books in the page using '{BookPageLocators.BOOK}'.")
        books = self.soup.select(locator)
        return [BookParser(book) for book in books]

    @property
    def last_page(self):
        logger.debug("Finding all number of catalogue pages available...")
        locator = BookPageLocators.PAGE_QUANTITY
        page_number_text = self.soup.select_one(locator).text
        logger.info(f"Found number of catalogue pages available: '{page_number_text}'.")
        last_page = int(re.search(r"[A-Za-z]+\s[\d]+[a-z\s]+([\d]+)", page_number_text).group(1))
        logger.debug(f"Extracted number of pages as integer: {last_page}'.")
        return last_page
