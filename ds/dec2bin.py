#!/usr/bin/python3

#Using a stack to implement decimal-to-binary calculator
import stack
def convert_dec2bin(value):
	rem_stack = stack.Stack()
	while value > 0:
		rem = value % 2
		rem_stack.push(rem)
		value = value //2
	bin_string = ''
	while not rem_stack.is_empty():
		bin_string = bin_string + str(rem_stack.pop())
	return bin_string

while True:
	num = int(input('Enter Number to Convert: '))
	print('%s in binary = %s' % (num,convert_dec2bin(num)))
