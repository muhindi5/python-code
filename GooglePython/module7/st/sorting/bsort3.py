#!/usr/bin/python3
# CS50:Bubblesort algorithm 
def bbsort(items):
    for x in range(len(items) - 1):
        for c in range(len(items) -1):
            if items[c] > items[c + 1]:
                 items[c],items[c + 1] = items[c + 1],items[c] #swap
            

items = [9,6,5,2,3]
print(items)
bbsort(items)
print(items)
