#!/usr/bin/python3

def get_algorithm_result(mlist):
    largest = mlist[0]
    for i in range(1,len(mlist)):
        if largest < mlist[i]:
            largest = mlist[i]
    return largest

def prime_num(value):
    if value <=1:
        return False
    for i in range(2,value):
        if value > value%i == 0:
            return False
    return True

items = [45,22,76,25,98,12,32,19,76,23]
items2 = [1,78,34,12,10,3]
str_items = ["apples","oranges","mangoes","banana","zoo"]
print('Items',items)
print('Largest = ',get_algorithm_result(items))
print('Items2',items2)
print('Largest = ',get_algorithm_result(items2))
print('str_items:',str_items)
print('Largest = ',get_algorithm_result(str_items))

test_vals = [15,23,54,3,-3,1,11,78,0,53,1001,13]
for x in range(len(test_vals)):
    print('Is prime?',test_vals[x],':',prime_num(test_vals[x]))

