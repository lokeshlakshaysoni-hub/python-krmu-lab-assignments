# Name: Lokesh Verma
# Project Title: Library Inventory Manager

import json
import logging

# LOGGING (TASK 5)
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# TASK 1 – BOOK CLASS
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"

# TASK 2 – INVENTORY
class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Book added: {book.title}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        for b in self.books:
            print(b)

# TASK 3 – JSON SAVE/LOAD
def save_to_file(inventory, filename="books.json"):
    try:
        data = [b.to_dict() for b in inventory.books]
        json.dump(data, open(filename, "w"), indent=4)
        logging.info("Saved to JSON file")
    except Exception as e:
        logging.error("Error saving file: " + str(e))


def load_from_file(inventory, filename="books.json"):
    try:
        data = json.load(open(filename))
        for d in data:
            inventory.add_book(Book(d["title"], d["author"], d["isbn"], d["status"]))
        logging.info("Loaded JSON file")
    except FileNotFoundError:
        logging.warning("JSON file not found. Starting empty inventory.")
    except Exception:
        logging.error("JSON file corrupted!")

# TASK 4 – SIMPLE CLI
def menu():
    print("\n=== Library Inventory Manager ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()
    load_from_file(inventory)

    while True:
        menu()
        choice = input("Choose option: ")

        try:
            if choice == "1":
                t = input("Title: ")
                a = input("Author: ")
                i = input("ISBN: ")
                inventory.add_book(Book(t, a, i))
                save_to_file(inventory)

            elif choice == "2":
                isbn = input("ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.issue():
                    print("Book issued.")
                    save_to_file(inventory)
                else:
                    print("Cannot issue!")

            elif choice == "3":
                isbn = input("ISBN to return: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.return_book():
                    print("Book returned.")
                    save_to_file(inventory)
                else:
                    print("Cannot return!")

            elif choice == "4":
                inventory.display_all()

            elif choice == "5":
                title = input("Enter title to search: ")
                results = inventory.search_by_title(title)
                for r in results:
                    print(r)
                if not results:
                    print("No matches found.")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid option!")

        except Exception as e:
            logging.error("Runtime error: " + str(e))
            print("Error occurred!")

if __name__ == "__main__":
    main()
