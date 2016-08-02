#!/usr/bin/python3
#data structures
mylist = []
print(mylist)
mylist.append(50) #add item to end of list
print(mylist)
mylist[len(mylist):] =[14,23,16,3,79,43,22,91] #appends the list at the end
print(mylist)
mylist.insert(2,69)#insert value 69 at index 2
print(mylist)
mylist.pop() #with no index removes last item
print(mylist)
mylist.remove(3) #remove item at index 3
print(mylist)
cp_list = mylist.copy() #return shallow copy of the list
mylist.clear() #removes all items from list, same as del l[:]
print(mylist)
print(cp_list.index(79)) #return index of first item with specified value
print(cp_list.count(22)) #number of times value appears in the list
cp_list.reverse() #reverse items in list
print(cp_list)
cp_list.sort() #sort items in the list
print(cp_list)

#using a list as a stack by using pop() and append() methods
mstack = [1,2,3,5,7]
mstack.pop() #remove last item in stack
mstack.append(4) #add item at end in stack
print(mstack)

#using lists as queues (FIFO)
from collections import deque
queue = deque(['Eric','John','Michael'])
queue.append('Becky') #Becky arrives
queue.append('Rex') #Rex arrives
queue.popleft() #first[Eric] in queue leaves
queue.popleft() #second[John] in queue leaves
print(queue)

#list comprehensions: create lists from operations or subsequences from operations
squares = []
for x in range(10):
    squares.append(x**2) #square of x
print(squares)

#same as
squares2 = [x**2 for x in range(10)]
print(squares2)

#combine ielements of 2 lists in not equal
print([(x,y) for x in (3,4,1) for y in (2,7,3) if x != y])

#similar to 
items = []
for x in [3,4,1]:
    for y in [2,7,3]:
        if x != y:
            items.append((x,y))
print(items)
            
#double numbers in list
vectors = [-3,-1,-4,-2]
print([x*2 for x in vectors])

#filter list to exclude numbers less than -3
print([p for p in vectors if p >-3])

#apply a function to all elements in the list
print([abs(a) for a in vectors])

#strip trailing spaces from list of items
fruits = [' passion fruit ','banana ','oranges ',' papaya',' lemon ']
print([f.strip() for f in fruits])
