import requests
import logging
import time

from milestone_3_Book_scraper.pages.book_page import BookPage

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt="%d-%m-%Y %H:%M:%S",
                    level=logging.INFO,
                    filename="logs.txt")

logger = logging.getLogger("scraping")

logger.info("Loading book list...")

page = BookPage(requests.get("https://books.toscrape.com/").content)
books = page.books


"""
scrape all pages into one byte object and pass it to BookPage
"""
# def meth_1():
page_content = b""
# global page
for page_number in range(2, page.last_page + 1):  # start with 2, because page 1 was scraped higher in the code
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    page_content += requests.get(url).content
logger.debug("Creating BookPage from page_content.")
page = BookPage(page_content)
books.extend(page.books)  # extend() adds to list each element of new iterable as a separate element, where as append()
# adds new iterable as one element

"""
scrape each page at a time and pass it to BookPage, than add books to books list
each implementation takes about equal time (42-43 secs)
"""
# def meth_2():
#     global page
#     for page_number in range(2, page.last_page + 1):
#         url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
#         logger.debug("Creating BookPage from page content.")
#         page = BookPage(requests.get(url).content)
#         books.extend(page.books)
#
#
# def measure_func(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(end - start)
#
#
# measure_func(meth_1)
# measure_func(meth_2)