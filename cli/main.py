from library_manager.inventory import LibraryInventory

def main():
    inventory = LibraryInventory()

    while True:
        print("\n===== Library Inventory Menu =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search by Title")
        print("6. Search by ISBN")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            inventory.add_book(title, author, isbn)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            if inventory.issue_book(isbn):
                print("Book issued!")
            else:
                print("Book cannot be issued (maybe already issued or not found).")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            if inventory.return_book(isbn):
                print("Book returned!")
            else:
                print("Cannot return book (maybe not issued or not found).")

        elif choice == "4":
            books = inventory.display_all()
            if books:
                print("\n--- All Books ---")
                for b in books:
                    print(b)
            else:
                print("No books found.")

        elif choice == "5":
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)
            for b in results:
                print(b)
            if not results:
                print("No matching books found.")

        elif choice == "6":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == "7":
            print("Thank you for using Library Manager!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

