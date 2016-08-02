#!/usr/bin/python3

def func1():
    '''This is the docstring of this function'''
    print('Function 1 executed')

#Get the documentation string of the function
print(func1.__doc__)
#Show all propeties available from the function
print('properties of the function: %s'%func1.__dir__())

#using type function to determine parameters in a function
def adder(val1,val2):
    print(type(val1))
    print(type(val2))
    if type(val1) == '<class \'str\'>':
        return val1
    elif type(val1) == '<class \'int\'>':
        return val1+val2
    else:
        return 'Cannot determine type'

#setting default parameters for functions
def stock_shelf(items=0,tag=''):
    new_shelf = {'items_count':items,'tag':tag}
    return new_shelf
 
#raising an error 
def get_num(number):
    if number > 0:
        return number*5
    else:
        raise ValueError('Invalid Value')

print(adder(23,34))
print(type('re'))
print(type('89'))
print(type(45))
print(type(65.34))

#create shelf 
shelf1 = stock_shelf(5,'Books') #provide param values
shelf2 = stock_shelf() #use default values in function args

print(shelf1)
print(shelf2)

print(get_num(-4))
print(get_num(7))
