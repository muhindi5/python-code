#!/usr/bin/python

import sys
#import Book
import bookstore

def initialise():
    print(sys.modules)#view all modules loaded
    description = {'title':'The Remake','author':'J. Kiuan','price':450.00}
    book = bookstore.Book(description)
    print(book.title)

def main():
    initialise()

if __name__ == '__main__':
    main()
