import re

from milestone_3_Book_scraper.locators.book_locators import BookLocators


class BookParser:

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
        locator = BookLocators.IMAGE
        return self.parent.select_one(locator).attrs["src"]

    @property
    def name(self):
        locator = BookLocators.NAME
        return self.parent.select_one(locator).attrs["title"]

    @property
    def link(self):
        locator = BookLocators.LINK
        return self.parent.select_one(locator).attrs["href"]

    @property
    def rating(self):
        locator = BookLocators.RATING
        classes = self.parent.select_one(locator).attrs["class"]
        rating = [r for r in classes if r != "star-rating"]
        if len(rating) > 0:
            return rating[0]
        return "No rating"

    @property
    def price(self):
        locator = BookLocators.PRICE
        price_text = self.parent.select_one(locator).text
        return float(re.search(r"[\d]+\.[\d]+", price_text).group())

    @property
    def availability(self):
        locator = BookLocators.AVAILABILITY
        return self.parent.select_one(locator).text.strip()
