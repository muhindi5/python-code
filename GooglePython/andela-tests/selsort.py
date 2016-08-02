#!/usr/bin/python3

def selsort(ls):
    for idx in range(len(ls)-1):
        #find index of the minimum value in the unsorted portion
        smallIdx = idx
        smallest = ls[idx]
        for i in range(idx+1,len(ls)):
            if ls[i] < smallest:
                smallest = ls[i]
                smallIdx = i
        #swap values at idx and smallIdx
        print('pass',idx,ls)
        ls[smallIdx],ls[idx] = ls[idx],smallest
#test
values = [11,7,12,14,19,1,6,18,8,20]
print('Before',values)
selsort(values)
print('After',values)
