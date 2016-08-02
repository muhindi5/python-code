#!/usr/bin/python

__all__ = ['describe'] #things to export

class Author:
    '''models the author of a book by first name, last name and email address'''
    def __init__(self,details):
        self.fname = details['fname']
        self.lname = details['lname']
        self.email = details['email']

    '''print a string representation of this object'''
    def describe(self):
        print('Author Detauls:\nFirst Name: %s\nLast Name: %s\nEmail: %s'
                %(self.fname,self.lname,self.email))

