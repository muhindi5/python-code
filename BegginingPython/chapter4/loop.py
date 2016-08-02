#!/usr/bin/python
def counter(number):
    counter = 0
    while counter < number:
        print(counter)
        counter+=1

def infinite():
    while True:
       number =  int(input('Enter the number:'))
       if number >10:
           print('Number too big')
           break #moves out of the most recent loop
       counter(200)
       
def ask():
    for i in range(10):
        age = input('Enter Age')
        if age < 18:
            print('Have a Juice')
            break
    else: #allowed in loops, only runs when loop does not complete due to break stmt
        print('You are underage')

#using a break statement
#Terminates the loop statement and transfers control to the statement immediately following the loop
def break_test():
    for letter in 'Kafkaesque':
        if letter == 'q':
            break
        print('printing letter: ',letter)
    else:
        print('Stopped at:',letter)

#Causes loop to skip remainder of the body and retest its condtion prior to iterating
def continue_test():
    for letter in 'Python':
        if letter == 'o':
            continue
        print('Current Letter:',letter)
    print('done')

break_test()
continue_test()
#infinite()

