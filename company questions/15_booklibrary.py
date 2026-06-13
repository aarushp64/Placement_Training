#define a class name 'book' that rpesents a book in a library. The class should have attributes like title, author, and publication year. And check for avalailaiblity and show the book which has max price 
#predifed books
mybooks = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye"]
myauthors=["F. Scott Fitzgerald", "Harper Lee", "George Orwell", "Jane Austen", "J.D. Salinger"]
myyears=[1925, 1960, 1949, 1813, 1951]
myavailability=["yes", "no", "yes", "yes", "no"]
myprices=[10.99, 12.99, 15.99, 9.99, 11.99]
class Book:
    def __init__(self,title,author,year,available,price):
        self.title=title
        self.author=author
        self.year=year
        self.available=available
        self.price=price

    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Publication Year:",self.year)
        print("Available:",self.available)
        print("Price:",self.price)
    def maxprice(self):
        maxprice=max(myprices)
        if self.price>maxprice:
            return self.price
        return maxprice
title=input("Enter the book title: ")
author=input("Enter the book author: ") 
year=int(input("Enter the publication year: "))
available=(input("Is the book available? (yes/no): "))
price=float(input("Enter the price: "))
book=Book(title,author,year,available,price)
book.display()
print("enter the book title to check availability: ")
check_title=input("Title: ")
    for b in mybooks:
        if mybooks.title.lower() == check_title.lower():
            if mybooks.check_availability():
                print("The book is available.")
            else:
                print("The book is not available.")
            break

print("The book with the maximum price is:", book.maxprice())