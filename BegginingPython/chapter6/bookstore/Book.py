#!/usr/bin/python3
class Book:
    '''This class implements a Book which has a title, author, price 
    genre and publisher
    Methods: 
    getTitle : returns book title
    getPrice : get price of the book
    getAuthor: returns the book author
    getGenre: returns the genre the book belongs to 
    getPublisher: returns the name of the book's publisher

    '''
    def __init__(self,bk_details):
        if type(bk_details).__name__ != type({}).__name__:
            raise TypeError("requires object of type dictionary, found %s" % type(bk_details))
        else:
            self.title = bk_details["title"]
            self.author = bk_details["author"]
            self.price = bk_details["price"]

def main():
              
    bk_desc = {"title":"The Cook","author":"J. Livid","price":500.00}
    book = Book(bk_desc)
    print('Price',book.price)
    print('Author',book.author)
    print('Title',book.title)
    print('Object Hash:',hash(book))
    print('Object Base class:',book.__class__.__base__)
if __name__ == "__main__":
    main()

