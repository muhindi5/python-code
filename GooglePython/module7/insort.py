#!/usr/bin/python3
# Insertion sort example


def insort(items):
    for index in range(1,len(items)):
        currentVal = items[index]
        position = index
        print('[outer] cv = %d; pos = %d' % (currentVal,position))
        while position > 0 and items[position-1] > currentVal:
            items[position] = items[position - 1]
            position  = position - 1
            items[position] = currentVal
            print('[inner] cv = %d; pos = %d' % (currentVal,position))

items = [98,12,54,30]
print(items)
insort(items)
print(items)

