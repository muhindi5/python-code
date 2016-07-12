#!/usr/bin/python3

# working with dictionary data structure

dict1 = {'name':'Allex','age':23,'proffession':'IT Security'}
dict2 = {'id':'a83bc27d9027e','amount':563.00,'state':'sent'}
print(dict1)
print('Name: ',dict1['name'])
print('Proffesion: ',dict1['proffession'])
print('Age: ',dict1['age'])

#loop through dict items 
for x in dict2.keys():
    print(x)

dict1['location'] = 'Milimani' #add new key to object
print(dict1)
del dict1['name'] #delete entry key 'name'
print(dict1)

#builtin methods for dictionary objects
print(dict2)
dict2.clear() # remove all elements from the object
print(dict2)
dict1.copy() # return a shallow copy of dictionary
dict1.items() #return turple of (key,value) pairs

print(dict1.items())
dict3  = {'status':'updated'}
dict1.update(dict3) #update items in dict1
print(dict1)

#alternative method on creating a dictionary object
foods = {}
foods['breakfast'] = '0700hrs'
foods['lunch'] = '1230hrs'
foods['snacks'] = '1600hrs'
foods['dinner'] = '2000hrs'
print(foods)
del foods['dinner']
print(foods)

