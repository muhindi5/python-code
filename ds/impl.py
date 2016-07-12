#!/usr/bin/python3 

# Test stack implentation

import stack

s = stack.Stack()
print(s.is_empty())
s.push(5)
s.push('man')
print(s.peek())

