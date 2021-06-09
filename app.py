import requests

from milestone_3_Book_scraper.pages.book_page import BookPage

page_content = requests.get("https://books.toscrape.com/").content
page = BookPage(page_content)

for book in page.books:
    print(book)