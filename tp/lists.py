#!/usr/bin/python3
# using lists 
list1 = ['Java','Python','Ruby','Perl','PHP']
list2 = [3,4,7,1,9,5,8]
list3 = ["Dell","Acer","Mac","HP","Lenovo"]

print(list1)
print(list2)
print(list3)

#print list sizes 
print('************************************************')
print('Size of list1: %d' % len(list1))
print('Size of list2: %d' % len(list2))
print('Size of list3: %d' % len(list3))

#get specific items in list
print('************************************************')
print(list1[2])
print(list2[:3])
print(list3[2:])
print(list1[1:1])
print(list2[:])
print(list2[-1]) #count from right 
print(list3[:len(list2)-5])

# updating list items
print('************************************************')
list1 [2] = 'NodeJS'
print('Updated list 1 has: %s ' % list1)

#update the list2 from item 4 with value 0
count = 3
for curr in list2:
    list2[count] = 0
    if count < (len(list2)-1):
        count = count + 1
            

print('Updated numbers list is: %s ' % list2)

#delete items in list
print('Items in list3 before delete: %s' % list3)
del list3[4]
print('Items in list3 after deleting item index 4: %s ' % list3)

# some basic list operations
print('************************************************')
numbers = [10,20,30,40]
numbers2 = [90,100,110,120]
greeting = ['Hello! ']
print(len(numbers)) #get the length of the list
print(numbers+numbers2) #concatenate 2 or more list items
greetings = greeting*5
print(greetings) #repeat list items
print('100 is found in the list: %s' % 100 in [numbers2]) #check for membership
#for x in numbers2:print(x) #iteration through list items
print(max(numbers2)) #get max value in the list
numbers2.append(130) # append item to end of the list
print(numbers2)
print(numbers2.count(100)) #get number of times 100 appears in the list
numbers3 = [45,23,87,45,12,23]
print(numbers3.index(12)) #get the lowest index the number 12 appears in
numbers3.reverse() #reverse items in the list
print('List reversed: %s ' % numbers3)
numbers3.sort() #sort numbers in list
print(numbers3)
numbers3.remove(87) #remove item from list
numbers3.insert(0,22) #insert item at index 0
print(numbers3)
current = numbers3.pop() #remove and return last object in the list
print('Last item in list %d' % current)
