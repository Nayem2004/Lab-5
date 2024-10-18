#Lab 5

class Book:
    def __init__(self, title, author, pages, read=False):
        #Initializes a book with a title, author, pages, and reading status.
        self.title = title
        self.author = author
        self.pages = pages
        self.read = read

    def description(self):
        #Returns a formatted string with book details.
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def mark_as_read(self):
        #Marks the book as read and prints a confirmation message.
        self.read = True
        print(f'You have now read "{self.title}"!')


class EbookReader:
    def __init__(self):
        #Initializes the EbookReader with a catalog and an empty library for each user.
        self.catalog = []
        self.library = []

    def add_to_catalog(self, book):
        #Adds books to the available catalog.
        self.catalog.append(book)

    def view_catalog(self):
        #Displays the list of books available for purchase.
        if not self.catalog:
            print("No books available in the catalog.")
        else:
            print("Available books in the catalog:")
            for i, book in enumerate(self.catalog, start=1):
                print(f"{i}. {book.description()}")

    def buy_book(self, book_number):
        #Buys a book from the catalog and adds it to the user's library.
        if 0 < book_number <= len(self.catalog):
            book = self.catalog[book_number - 1]
            self.library.append(book)
            print(f'You have purchased "{book.title}"!')
        else:
            print("Invalid book number.")

    def view_library(self):
        #Displays the list of purchased books.
        if not self.library:
            print("Your library is empty.")
        else:
            print("Your library:")
            for i, book in enumerate(self.library, start=1):
                print(f"{i}. {book.description()}, Read: {'Yes' if book.read else 'No'}")

    def read_book(self, book_number):
        #Marks a book from the library as read.
        if 0 < book_number <= len(self.library):
            book = self.library[book_number - 1]
            book.mark_as_read()
        else:
            print("Invalid book number.")


def main():
    #Main function to run the e-book reader system.
    reader = EbookReader()

    # Adds public domain books to the catalog.
    reader.add_to_catalog(Book("Moby Dick", "Herman Melville", 635))
    reader.add_to_catalog(Book("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", 307))
    reader.add_to_catalog(Book("Dracula", "Bram Stoker", 418))

    while True:
        print("\nWelcome to the E-Book Reader!")
        print("1. View Catalog")
        print("2. Buy a Book")
        print("3. View Your Library")
        print("4. Read a Book")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

        if choice == '1':
            reader.view_catalog()

        elif choice == '2':
            reader.view_catalog()
            try:
                book_number = int(input("Enter the number of the book you want to purchase: "))
                reader.buy_book(book_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            reader.view_library()

        elif choice == '4':
            reader.view_library()
            try:
                book_number = int(input("Enter the number of the book you want to read: "))
                reader.read_book(book_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Thank you for using the E-Book Reader. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()