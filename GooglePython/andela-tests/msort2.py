#!/usr/bin/python3
def mergesort(a_list):
    print('splitting list...',a_list)
    if len(a_list) > 1:
        mid = len(a_list)//2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]
        #recursive call to split list further
        mergesort(lefthalf)
        mergesort(righthalf)
        
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a_list[k] = lefthalf[i]
                i = i+1
            else:
                a_list[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            a_list[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            a_list[k] = righthalf[j]
            j = j+1
            k = k+1
    print('Merging',a_list)

mylist = [21,1,26,45,29,28,2,9,16,49,39,27,43,34,46,40]
print('Before',mylist)
mergesort(mylist)
print('After',mylist)


