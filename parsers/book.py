import logging
import re
import logging

from milestone_3_Book_scraper.locators.book_locators import BookLocators

logger = logging.getLogger("scraping.book_parser")


class BookParser:

    RATINGS = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, parent):
        logger.debug(f"New book parser created from '{parent}'.")
        self.parent = parent

    def __repr__(self):
        star = "stars" if self.rating > 1 else "star"
        return f"""
        <Book: {self.name}, 
        rating: {self.rating} {star}, 
        price: {self.price}, 
        availability: {self.availability}
        image: {self.image},
        link: {self.link}>"""

    @property
    def image(self):
        logger.debug("Finding the book image...")
        locator = BookLocators.IMAGE_LOCATOR
        book_image = self.parent.select_one(locator).attrs["src"]
        logger.debug(f"Found book image: '{book_image}'.")
        return book_image

    @property
    def name(self):
        logger.debug("Finding the book name...")
        locator = BookLocators.NAME_LOCATOR
        book_name = self.parent.select_one(locator).attrs["title"]
        logger.debug(f"Found book name: '{book_name}'.")
        return book_name

    @property
    def link(self):
        logger.debug("Finding the book link...")
        locator = BookLocators.LINK_LOCATOR
        book_link = self.parent.select_one(locator).attrs["href"]
        logger.debug(f"Found book link: '{book_link}'.")
        return book_link

    @property
    def rating(self):
        logger.debug("Finding the book rating...")
        locator = BookLocators.RATING_LOCATOR
        classes = self.parent.select_one(locator).attrs["class"]
        rating_class = [r for r in classes if r != "star-rating"]
#       rating_class = filter(lambda x: x != 'star-rating', classes)
        rating_number = BookParser.RATINGS.get(rating_class[0])
        logger.debug(f"Found book rating: '{rating_number}'.")
        return rating_number

    @property
    def price(self):
        logger.debug("Finding the book price...")
        locator = BookLocators.PRICE_LOCATOR
        price_text = self.parent.select_one(locator).text
        price_float = float(re.search(r"[\d]+\.[\d]+", price_text).group())
        logger.debug(f"Found book price: '{price_float}'.")
        return price_float

    @property
    def availability(self):
        logger.debug("Finding the book availability...")
        locator = BookLocators.AVAILABILITY_LOCATOR
        book_availability = self.parent.select_one(locator).text.strip()
        logger.debug(f"Found book availability: '{book_availability}'.")
        return book_availability
