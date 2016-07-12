class Shelf:
    '''class Shelf models a library shelf.
    Books can be added, removed, rearranged
    probed for details.
    Methods: 
    addOne: adds 1 book to the shelf
    addMany: adds more than 1 book to the shelf
    getOne: returns 1 book
    getMany: returns many books
    '''
    
    def __init__(self,books={}):
        '''optional passing of initial dictionary of books'''
        if type(items) != type({}):
                raise TypeError('Shelf requires a dictionary but was given %s' % type(books))
        self.books = books
        return

