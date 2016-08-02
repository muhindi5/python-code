#!/usr/bin/python3

#get type/class of a number
numbers = [2,43.234324,8j]
for i in range(len(numbers)):
    print('Number',numbers[i],'is of',type(numbers[i]))

#format specifiers for numbers
print('Python uses the % character to format variable for output eg. %f,%E,%d\n')
for x in range(len(numbers)-1):
    print('\n') 
    print('Formatted as an integer:%d = %d' % (numbers[x],numbers[x]))
    print('Formatted as a float :%d = %.2f' % (numbers[x],numbers[x]))#2decimals specified
    print('Formatted as a Exponential :%d = %E' % (numbers[x],numbers[x]))
    print('Formatted as a Octal:%d = %o' % (numbers[x],numbers[x]))
    print('Formatted as a Hex:%d = %x' % (numbers[x],numbers[x]))

print('\n')

#basic math
print(4//2) #output will be int 
print(4/2) #output will be float
print(4.0/2.0) #output will be float
print(4%2) #output will be 0 (modulus)i
print('Exchange Rate: Kshs %.4f' % 8920.32432008)
print('Exchange Rate: Kshs %.022f' % 8920.32432008)

#printing numbers(0 - 20) in octal and in hex
print('*'*40)
print('Decimal\tHex\tOctal')
print('*'*40)
for n in range(21):
    print('%d\t%x\t%o' % (n,n,n))
