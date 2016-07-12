#Loop though a phrase counting occurences of a letter.
count = 0
words = 'Ask not for who the bell tolls, It tolls for thee!'
for ch in words:
    if ch == 'e':
        count = count + 1
print('Number of \'e\'s\' in the sentence %s: %d' % (words,count))

#using a while loop
#Access every third element in a loop
items = [2,65,43,232,0,9,64,76,32,45,7,86]
i = 0
while i < len(items):
    print(items[i])
    i = i + 3

#For-In demo
mylist = ['bread','milk','butter']
for current  in mylist:
    print(current)

