class Book:
    def __init__(self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name


class Library:
    def __init__(self, library_id, address, book_list):
        self.library_id = library_id
        self.address = address
        self.book_list = book_list

    def count_books(self, char):
        count = 0
        for book in self.book_list:
            if book.book_name.

    def remove_books(self, book_list):
        pass


book1 = Book(100, 'C++ Programming')
book2 = Book(200, 'Introduction to SQL')
book3 = Book(300, 'Core Java')
books = [book1, book2, book3]

