from bs4 import BeautifulSoup
from milestone_3_Book_scraper.locators.book_page_locators import BookPageLocators
from milestone_3_Book_scraper.parsers.book import BookParser


class BookPage:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def books(self):
        locator = BookPageLocators.BOOK
        books = self.soup.select(locator)
        return [BookParser(book) for book in books]
