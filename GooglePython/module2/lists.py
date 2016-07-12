# working with lists
genres = ['reggae','hip-hop','rock','EDM','folk','alternative','deep house']
print('-'*10)
print(genres)
#Add item at end of list
genres.append('indie-pop')
print('-'*10)
print(genres)
#Insert item at index 4
genres.insert(3,'heavy-metal')
print('-'*10)
print(genres)
#Append new list to previous
genres.extend(['afro-jazz','pop','fusion'])
print('-'*10)
print(genres)
#Remove an item from the list..may throw ValueError if item not found
#for-in can be used to check
genres.remove('pop')
print('-'*10)
print(genres)
#sort the list
genres.sort()
print('-'*10)
print(genres)
#reverse items in the list
genres.reverse()
print('-'*10)
print(genres)
#remove item at specific index
genres.pop(4)
print('-'*10)
print(genres)
genres[0:2] = 'afro-jazz'
print('-'*10)
print(genres)

