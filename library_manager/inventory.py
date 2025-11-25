import json
from pathlib import Path
import logging
from .book import Book

logging.basicConfig(filename="library.log", level=logging.INFO)

class LibraryInventory:
    def __init__(self, file_path="data/catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**book) for book in data]
            else:
                self.save_data()
        except Exception as e:
            logging.error("Error loading file: %s", e)
            self.books = []

    def save_data(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
        except Exception as e:
            logging.error("Error saving data: %s", e)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_data()
        logging.info(f"Book added: {title}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books

