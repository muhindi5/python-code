#!/usr/bin/python3

class Author(object):
    '''Models a book authors details'''
    __init__(self,details):
        self.fName = details['fName']
        self.lName = details['lName']
        self.age = details['age']
        self.description = {"fname":self.fName,"lname":self.lname,"age":age}

    update(self,data):
        '''update the author details in the instance obj'''
        self.description = data

