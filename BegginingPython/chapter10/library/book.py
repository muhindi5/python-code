#!/usr/bin/python3
'''Module 'book' models a library book item and its related domain objects and 
exception classes'''

from author import Author

class Book:
    '''Models a Book with description including title,author,genre and price'''
    
    def __init__(self,title='Unknown', genre='general',authorDetails={},price=00.00):
        self.title = title
        self.genre  = genre
        self.author = Author(authorDetails)
        self.price = price

    '''Print the details of the book and author objects'''
    def describe(self):
        print('Book Details\nTitle:%s\nGenre:%s\nAuthor:%s\nPrice:%s' 
                % (self.title,self.genre,self.author.describe(),self.price))

def main():
    authorDetails = {'fname':'Sam','lname':'Harris','email':'harris_s@wup.com'}
    book = Book('Letter to a Christian Nation','Philosophy',authorDetails,1450.00)
    book.describe()

if __name__ == '__main__':
    main()

