#!/usr/bin/python3

def selector_sort(items):
    for i in range(len(items)):
        #assume the ith element is the smallest
        smallest = i
        for j in range(i+1,len(items)):
            #determine if any other element contains a smaller value
            if items[j] < items[smallest]:
                smallest = j
        if items[smallest] !=i:
            items[smallest],items[i] = items[i],items[smallest]

n = [23,54,12,65,33,76,22]
print('Before: ',n)
selector_sort(n)
print('After: ',n)
