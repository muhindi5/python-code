#!/usr/bin/python3
def bsorted(items):
    for num in range(len(items)):
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i +1] = items[i+1], items[i]

#test
n = [23,54,12,65,33,76,22]
print('Before: ',n)
bsorted(n)
print('After: ',n)
