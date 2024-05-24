class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author, price, and rating.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        :param rating: book's rating
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has a name and a rating.

        :param name: book store name
        :param rating: book store rating
        """
        self.name = name
        self.rating = rating
        self.books = []  # A list to store books present in the store

    def can_add_book(self, book: Book) -> bool:
        """
        Check if a book can be added to the store.

        It is possible to add a book to the store if:
        1. The book with the same author and title is not yet present in this store.
        2. The book's rating is greater than or equal to the store's rating.

        :param book: Book
        :return: bool
        """
        for stored_book in self.books:
            if stored_book.title == book.title and stored_book.author == book.author:
                return False  # Book with same title and author already exists
        return book.rating >= self.rating

    def add_book(self, book: Book):
        """
        Add a new book to the store if possible.

        :param book: Book
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if a book can be removed from the store.

        A book can be successfully removed if it is actually present in the store.

        :param book: Book
        :return: bool
        """
        return book in self.books

    def remove_book(self, book: Book):
        """
        Remove a book from the store if possible.

        :param book: Book
        """
        if self.can_remove_book(book):
            self.books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in the current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self.books, key=lambda x: x.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of books with the highest rating.

        :return: list of Book objects
        """
        max_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == max_rating]

if __name__ == '__main__':
    # Testing the Book and Store classes
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99, 4.5)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 10.99, 4.8)
    book3 = Book("1984", "George Orwell", 9.99, 4.7)

    store = Store("Book Emporium", 4.6)
    
    # Adding books to the store
    store.add_book(book1)
    store.add_book(book2)
    store.add_book(book3)
    
    # Displaying all books in the store
    print("All books in the store:")
    for book in store.get_all_books():
        print(f"{book.title} by {book.author} - ${book.price} - Rating: {book.rating}")

    # Displaying books ordered by price
    print("\nBooks ordered by price:")
    for book in store.get_books_by_price():
        print(f"{book.title} - ${book.price}")

    # Displaying the most popular book(s)
    print("\nMost popular book(s):")
    for book in store.get_most_popular_book():
        print(f"{book.title} by {book.author} - Rating: {book.rating}")
