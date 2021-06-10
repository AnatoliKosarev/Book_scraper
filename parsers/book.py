import re

from milestone_3_Book_scraper.locators.book_locators import BookLocators


class BookParser:

    RATINGS = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"""
        <Book: {self.name}, 
        rating: {self.rating}, 
        price: {self.price}, 
        availability: {self.availability}
        image: {self.image},
        link: {self.link}>"""

    @property
    def image(self):
        locator = BookLocators.IMAGE_LOCATOR
        return self.parent.select_one(locator).attrs["src"]

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        return self.parent.select_one(locator).attrs["title"]

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        return self.parent.select_one(locator).attrs["href"]

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        classes = self.parent.select_one(locator).attrs["class"]
        rating_class = [r for r in classes if r != "star-rating"]
        rating_number = BookParser.RATINGS.get(rating_class[0])
        return rating_number

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        price_text = self.parent.select_one(locator).text
        return float(re.search(r"[\d]+\.[\d]+", price_text).group())

    @property
    def availability(self):
        locator = BookLocators.AVAILABILITY_LOCATOR
        return self.parent.select_one(locator).text.strip()
