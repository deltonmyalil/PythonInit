class Library:
    def __init__(self, bookName, author, number):
        self.bookName = bookName
        self.author = author
        self.number = number

    def getBook(self):
        print("Enter Book details:")
        self.bookName = input("Enter Book Title>>>")
        self.author = input("Enter Author's name>>>")
        self.number = int(input("Enter Book ID number>>>"))

    def printBook(self):
        print("The book is titled", self.bookName, "written by", self.author, "\nBookID is", self.number)


HP = Library("NULL", "NULL", 0)
HP.getBook()
HP.printBook()
