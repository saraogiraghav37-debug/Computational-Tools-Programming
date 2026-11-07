# Library Management System using inheritance and polymorphism

class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.issued = False
    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued successfully.")
        else:
            print("Already issued.")
    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned successfully.")
        else:
            print("Item was not issued.")
    def display(self):
        print("Title:", self.title)

class Book(LibraryItem):
    def display(self):
        print("Book:", self.title)

class Magazine(LibraryItem):
    def display(self):
        print("Magazine:", self.title)

class Journal(LibraryItem):
    def display(self):
        print("Journal:", self.title)

# Creating objects
book = Book("Python Programming")
magazine = Magazine("Science Today")
journal = Journal("AI Research")

# Polymorphism
items = [book, magazine, journal]
print("Library Items:")
for item in items:
    item.display()
print("\nIssue and Return Operations:")
book.issue()
book.return_item()
magazine.issue()
journal.issue()