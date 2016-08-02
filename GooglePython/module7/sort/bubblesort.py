#!/usr/bin/python3

def bubblesorter(nlist):
    for current in range(len(nlist)-1, 0, -1):
        for i in range(current):
            if nlist[i] > nlist[i+1]:
                nlist[i],nlist[i+1] = nlist[i+1],nlist[i] #swap
    return my_items

my_items = [23,45,26,76,98,12,34,66,96]
print('Unsorted: ',my_items)
print('Sorted: ',bubblesorter(my_items))
