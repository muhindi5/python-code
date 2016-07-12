# lists additional...(check more in module 3)

print('\n\n\n#-------------------Using lists-------------#')
numbers = [1,3,5,6,7]
print(numbers)
#multiply every number in the list above
numbers2 = [x*2 for x in numbers]
print(numbers2)

""" Sets
Unordered collection with no duplicates
Duplicate items in a set are removed
Can be created using the keyword set or {} braces
NB: set() creates an empty set while {} alone create an empty dictionary
NB: set construct accepts one argument a  list
"""
mylist = [3,5,7,2,8,1]
myset = set(mylist)
print('\n\n\n#-------------------Using sets-------------#')
print(myset)

# create set using braces
set2 = {32,45,23,76,12,11,87}
print(set2)

#operations on sets
set1 = set([1,2,3])
set3 = set([23,82,3])
set2 = set([5,7,9])
print(set1 | set2) #union
print(set1 & set3) #intersection

#set comprehensions
vowels = ['a','e','i','o','u']
print({x for x in 'derisive' if x not in vowels}) # find all consonants in a word

#create an immutable set 
fset = frozenset([84,321,55]) # immutable set

print('\n\n\n#-------------------Using Turples-------------#')
#immutable and output is surrounded by parentheses
#can hold immutable objects/data
#performance is good due to immutability
#empty () creates an empty turple, creating a tuple with 1 elmenent requires a trailing ,
t1 = ()
t2 = ('a',) #
t3 = ('a','b','c','34',[45,'tester','A'])
print(t3)

print('\n\n\#------------------Using Dictionaries-------------#')
#represented by key value pairs
#keys can of any immutable type and unique 
#values can be of any type mutable or immutable
#can be made by using curly braces 
interests = {1:'bitcoin',2:'odoo',3:'linux',4:'github'}
print(interests)
#create a dictionary using a comprehension
#print({x:x.reverse() for x in interests[x]})
print({x:x*10 for x in [2,6,8,9,3,5]})

#dict keyword can also be used
print(dict([(1,'a'),(2,'b'),(3,'c')]))

#get values in a dictionary
print('Items in dictionary object)')
for current in interests:
    print(interests[current])
#delete item in dict object
del(interests[1])
for current in interests:
    print(interests[current])
#inbuilt methods in dictionary
#keys(), values(), iteritems(), itervalues(), has_key()
print('Keys in dictionary object')
print(interests.keys())
print('values in dictionary object')
print(interests.values())

#iterate through a dict
for k, v in interests().iteritems():
    print(k,v)


