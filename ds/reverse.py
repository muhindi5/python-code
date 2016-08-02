#!/usr/bin/python3
# Function that uses a stack to reverse the characters of a sting

import stack

def rev_str(istr):
    stk = stack.Stack()
    
    #push each character in the string into the stack
    for i in istr:
        stk.push(i)
    return stk

x = input('Enter string to be reversed: ')
out_stack = rev_str(x)
reversed_str = ''
while not (out_stack.is_empty()):
    reversed_str +=out_stack.pop()
print(reversed_str)


