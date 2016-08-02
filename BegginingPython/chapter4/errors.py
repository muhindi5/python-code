#!/usr/bin/python
#check presence of an item in a dictionary instance
def is_present(target,container):
    '''Checks the presence of an item in a dictionary'''
    try:
        if container[target]:
            print('Item Found')
    
    #no such key in the container
    except KeyError as error:
        print('%s --> No such item in the list' % error)

    #wrong type for key
    except TypeError:
        pass

    #will only run when no exceptions have been caught ie. all goes well
    else:
        print('Finished search')


def main():
    shopping_list = {'eggs':20,'milk':3,'bread':1,'butter':3}
    is_present('yeast',shopping_list)
    print('docstring in function %s --> %s' % is_present('',shopping_list).__name__(),is_present('',shopping_list).__doc__())

if __name__ == '__main__':
    main()

