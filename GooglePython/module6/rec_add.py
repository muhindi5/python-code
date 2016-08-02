#!/usr/bin/python3
def adder(value):
    if value == 1:
        return 1
    else:
       return (value + adder(value-1))

#using list slices to recursively add all numbers in the list
def list_sum(num_list):
    if len(num_list) == 1: #check if list is 1 element long
        return num_list[0] 
    else:
        return num_list[0] + list_sum(num_list[1:])
#using recursion to print in integer from 1 to n in reverse 
def print_rev(n):
    if n > 0:
        print (n,)
        print_rev(n -1)
    

print(adder(5))
print(list_sum([2,5,7,8]))
num = int(input('Enter number to reverse from: '))
print('printing 1 to %d in reverse:\n' % num)
print_rev(num)
