
class Book:
    def __init__(self, title, author, borrowed=False):
        self.title = title
        self.author = author
        self.borrowed = borrowed

    def __str__(self):
        status = "Ödünç Alındı" if self.borrowed else "Mevcut"
        return f"{self.title} - {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Kitap eklendi: {title} - {author}")

    def borrow_book(self, book_index):
        if 0 <= book_index < len(self.books):
            if not self.books[book_index].borrowed:
                self.books[book_index].borrowed = True
                print(f"Kitap ödünç verildi: {self.books[book_index].title}")
            else:
                print("Bu kitap zaten ödünç alınmış!")
        else:
            print("Geçersiz kitap indexi!")

    def return_book(self, book_index):
        if 0 <= book_index < len(self.books):
            if self.books[book_index].borrowed:
                self.books[book_index].borrowed = False
                print(f"Kitap geri alındı: {self.books[book_index].title}")
            else:
                print("Bu kitap zaten kütüphanede!")
        else:
            print("Geçersiz kitap indexi!")

    def list_books(self):
        print("\nMevcut Kitaplar:")
        for i, book in enumerate(self.books):
            if not book.borrowed:
                print(f"{i}: {book}")

        print("\nÖdünç Alınan Kitaplar:")
        for i, book in enumerate(self.books):
            if book.borrowed:
                print(f"{i}: {book}")


