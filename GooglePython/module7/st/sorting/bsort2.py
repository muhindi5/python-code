# Using bubblesort

def bsort(items):
    # go through the items...
    for i in range(len(items) -1):
        #go through all the elements in loop i
        for j in range(i):
            if items[j] > items[j+1]:
                    items[j],items[j+1] = items[j+1],items[j]
    return items


items = [23,45,76,12,34,14,67,33,25,41]
print('Items in list:'+str(items))
bsort(items)
print('Sorted items in list:'+str(items))

