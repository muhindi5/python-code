# Implementation of a stack ADT
class Stack:
    def __init__(self):
        self.items = []

    '''Check if stack is empty'''
    def is_empty(self):
        return self.items == []

    '''add item to stack'''
    def push(self,item):
        self.items.append(item)

    '''remove item from stack'''
    def pop(self):
        return self.items.pop()

    '''check if item is in list'''
    def peek(self):
        return self.items[len(self.items) - 1]

    '''get size of items in stack'''
    def size(self):
        return len(self.items)


