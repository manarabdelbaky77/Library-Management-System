books = []
members = []

def show_books():
    if not books:
        print("No books available.")
        return
    print(" Book List:")
    for book in books:
        status = "Available" if book["available"] else "Not Available"
        print(f'{book["id"]} - {book["title"]} by {book["author"]} [{status}]')
    print()

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    books.append({"id": book_id, "title": title, "author": author, "available": True})
    print(" Book added successfully!")

def register_member():
    member_id = input("Enter member ID: ")
    name = input("Enter member name: ")
    members.append({"id": member_id, "name": name})
    print(" Member registered successfully!")

def borrow_book():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print(" Book borrowed successfully!")
            else:
                print("Book is currently not available")
            return
    print(" Book not found")

def return_book():
    book_id = input("Enter book ID to return: ")
    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            print(" Book returned successfully!")
            return
    print("Book not found")

while True:
    print("**Library Management System**")
    print("1. Show all books")
    print("2. Add a new book")
    print("3. Register a new member")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        register_member()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")
