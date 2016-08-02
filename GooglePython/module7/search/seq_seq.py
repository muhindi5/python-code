#!/usr/bin/python3

'''search sequentially for an item in the list'''
def sequential_search(alist,item):
    position = 0
    found = False
    while position < len(alist) and not found:
        if alist[position] == item:
            found = True
        else:
            position = position + 1
    return found

numbers  = [3,7,3,2,8,5,6]
state = sequential_search(numbers,3)
print(state)

def ordered_sequential_search(alist,item):
    position = 0
    found = False
    stop = False

    while position < len(alist) and not found and not stop:
        if alist[position] == item:
            found = True
        elif alist[position] > item:
            stop = True
        else:
            position = position + 1
    return found

numbers2 = [2,4,6,7,9,12,15,19,22]
state = ordered_sequential_search(numbers2,879)
print(state)
