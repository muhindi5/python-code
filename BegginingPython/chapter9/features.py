#!/usr/bin/python3

#using lambdas : python special word that creates a function and uses it in place
#print even numbers
numbers = [45,23,65,22,42,12,65,87,98]
result = filter(lambda x: x%2==0,numbers)
#altnative
func = lambda x:x%2 == 0
result2 = filter(func,numbers)
print(result2)

#maps:short circuiting loops
map_me = ['a','b','c','d','e','f','g']
result = map(lambda x: 'The letter is %s' % x,map_me)
print(result)

#list comprehensions
numbers = [43,12,54,32,77,34,98,12,65,23,68,23]
print([x for x in numbers if x%2 == 0])
