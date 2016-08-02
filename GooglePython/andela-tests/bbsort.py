#!/usr/bin/python3

def bsort(values):
    for i in range(len(values)-1):
        for x in range(len(values)-1-i):
            if values[x] > values[x+1]:
                values[x],values[x+1] = values[x+1],values[x]
        print('Pass',i+1,values)
#tester
numbers = [19,1,9,7,3,10,13,15,8,12]
print('Unsorted:',numbers)
bsort(numbers)
print('Sorted: ',numbers)
