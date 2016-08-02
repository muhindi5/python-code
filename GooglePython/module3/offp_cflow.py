#!/usr/bin/python3
# control flow

x = int(input('Enter an integer: '))
if x < 10:
    print('Less than 10')
elif x == 10:
    print('Nicely done')
elif x > 10:
    print('Too Big')
else:
    print('More')

words = ['cats','dogs','tigers','lions']
for w in words:
    print(w,len(w))
#remove all words longer than 4 characters from list
count  = 0
for word in words:
    if len(word) > 4:
        words[count] = ''
        count +=1
print(words)

#range
a = ['Some','Funny','colored','Beans']
for x in range(len(a)):
    print(x, a[x])

#break, continue and else clauses in loops
#look for prime numbers
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n,'equals',x,'*',n//x)
            break
        else:
            #loop fell through without finding a factor
            print(n, 'is a prime number')

#using continue
for num in range(2,10):
    if num % 2  == 0:
        print('Found even number',num)
        continue #go to next iteration of loop
    print('Found an odd number',num)

#using pass #create a syntactic placeholder. does nothing
#can be used to create minimal classes or empty function
def do_later(x1,y1):
    pass #implement later

class Empty:
    pass #empty class     

#defining functions
def fib(n):
    '''Print a Fibonacci series upto n'''
    a,b = 1,1
    while a < n:
        print(a), 
        a, b = b,a+b
    print()
fib(200)

#default argument values
def ask(prompt,retries=4,complaint='Yes or No Please'):
    while True:
        ok = input(prompt)
        if ok in ('y','yes','ye'): #test whether a sequence contains a certain value
            return True
        if ok in ('n','no','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('Uncooperative user')
        print(complaint)
#options in calling this function
display_tx = 'Do you want to exit'
ask(display_tx,2,'Please Type Yes or No')
ask(display_tx,3)
ask('Do you want to exit')
