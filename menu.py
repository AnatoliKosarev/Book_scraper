import logging

from milestone_3_Book_scraper.app import books

logger = logging.getLogger("scraping.menu")

MENU_MESSAGE = """\nPlease select your option:
- 'b': to display 10 best rated books
- 'c': to display 5 cheapest books
- 'n': to display the next book in the collection
- 'q': to exit

Enter your option here: """

book_generator = (book for book in books)  # generates next(iterable) value from books


def print_ten_best_rating_books():
    logger.info("Finding best rated books...")
    # ten_best_rating_book_list = sorted(books, key=lambda b: b.rating, reverse=True)[:10]
    """ reverse=True - because default order is ASC (0-100), to display max rating first we have to reverse order
    we use slicing [:10] to display first 10 sorted elements
    we can also sort by more than one parameter, e.g. first sort by rating, after that, sort values for each rating
    by price
    """
    ten_best_rating_book_list = sorted(books, key=lambda b: (b.rating * -1, b.price))[:10]
    """
    b.rating * -1 - because we can't use reverse=True anymore, because than prices will be sorted from max to min
    so we use b.rating * -1 to sort rating from max to min and prices are sorted from min to max (ASC) order by default
    rating 1, 3, 5 * -1 = -5, -3, -1 for ASC order
    """
    print("\n--10 best rated books--")
    for book in ten_best_rating_book_list:
        print(book)


def print_five_cheapest_books():
    logger.info("Finding cheapest books...")
    five_cheapest_book_list = sorted(books, key=lambda b: b.price)[:5]
    print("\n--5 cheapest books--")
    for book in five_cheapest_book_list:
        print(book)


def print_next_book():
    logger.info("Getting next book from generator of all books...")
    print(next(book_generator))


options = {
    "b": print_ten_best_rating_books,
    "c": print_five_cheapest_books,
    "n": print_next_book
}


def start_menu():
    user_selection = input(MENU_MESSAGE)
    while user_selection != "q":
        if user_selection in options:
            selected_option = options[user_selection]
            selected_option()
        else:
            print("Invalid selection. Please try again.")

        user_selection = input(MENU_MESSAGE)
        logger.debug("Terminating program...")


start_menu()
