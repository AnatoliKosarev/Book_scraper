import re
from bs4 import BeautifulSoup

from milestone_3_Book_scraper.locators.book_page_locators import BookPageLocators
from milestone_3_Book_scraper.parsers.book import BookParser


class BookPage:

    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books(self):
        locator = BookPageLocators.BOOK
        books = self.soup.select(locator)
        return [BookParser(book) for book in books]

    @property
    def last_page(self):
        locator = BookPageLocators.PAGE_QUANTITY
        page_number_text = self.soup.select_one(locator).text
        return int(re.search(r"[A-Za-z]+\s[\d]+[a-z\s]+([\d]+)", page_number_text).group(1))
