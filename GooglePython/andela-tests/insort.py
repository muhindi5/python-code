#!/usr/bin/python3

def insort(ls):
    for idx in range(1,len(ls)):
        for x in range(idx,0,-1):
            if ls[x-1] <= ls[x]:
                break #values are in place
            ls[x],ls[x-1] = ls[x-1],ls[x] #swap
        print('Pass',idx,ls,'\tls[x]=',ls[x],'\tls[x-1]=',ls[x-1])
#test
numbers = [15,5,4,18,12,19,14,10,8,20]
print('Before:',numbers)
insort(numbers)
print('After',numbers)
