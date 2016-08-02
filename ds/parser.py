#!/usr/bin/python3
# Implementing a parenthesis balance parser using a stack
# process a string of parentheses from left to right
# if opening parenthsis push into stack indicating that closing p
#will appear later if closing parenthesis, pop stack, the parentheses are balenced if its possible to pop the stack to match every closing parenthesis

import stack

def parens_parser(str_parens):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(str_parens) and balanced:
        symbol = str_parens[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index +=1
    if balanced and s.is_empty():
        return True
    else:
        return False

#test the function
print(parens_parser('((()()(())))))))'))
print(parens_parser('()(())'))
