#!/usr/bin/python3
'''Binary search algorithm impl.'''
def binary_search(nlist,item):
    first = 0
    last = len(nlist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) //2
        print(midpoint)
        if nlist[midpoint] == item:
            found = True
        elif item < nlist[midpoint]:
                last = nlist[midpoint]+1
        else:
            first = nlist[midpoint] + 1
    return found
state = binary_search([4,6,7,9,12],5)
print(state)
