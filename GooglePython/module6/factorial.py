#!/usr/bin/python3
#Find factorial of a number using recursion
def get_fact(x):
    '''recursive function gets the factorial of a number'''
    if x == 1:
        return 1
    else:
        return (x * get_fact(x-1))
num = int(input('Enter a number: '))
if num > 0:
    print('Factorial of %d is %d: ' % (num,get_fact(num)))


