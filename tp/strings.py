#!/usr/bin/python3
# working with strings
word = 'Strings are the most common data type in Python'
print(word)
#accessing substrings
sb1 = word[0:6]
sb2 = word[15:21]
sb3 = word[23:]
print('characters in word[0:6]: %s' % sb1)
print('characters in word[15:21]: %s' % sb2)
print('characters in word[23:]: %s' % sb3)

#updating strings
sb4 = 'Hello'
print(sb4[:5]+'\n'+'World')
bt_price = 2045.500000
usd_price = .0023493243
print('The exchange rate of 1 bitcoin is %3.2f dollars' % bt_price)
print('The exchange rate of 1 dollar is 0%.5f bitcoin' % usd_price)

#printing string 
qstr = '''This is a multiline string \n and is printed 
as is. All special characters are printed\t out as
is in the string as in\n string.'''
print (qstr)

#using a raw string
# raw strings ignore special characters and print the string as is.
rawstr = r'some string \n this is'
print(rawstr)

#Unicode strings
#strings in python stored as 8-bit ASCII, Unicode strings are 16-bit 
ustr = u'This string is in Unicode format'
print(ustr)

#in-built string functions
print(rawstr.capitalize()) #capitalises the first letter of the string
print('In the string \'%s\', letter \'t\' occurs %d times.' % (ustr,ustr.count('t',0,len(ustr)))) #find a substring in the string 
print('Size of the string is: %d' % len(qstr)) #get the length of a string
print('Tokens after spliting \'%s\': %s' % (ustr,ustr.split(' ',len(ustr)))) #creates word tokens and returns list containing tokens
print('Swapping case for the string \'%s\' results in \'%s\''% (ustr,ustr.swapcase())) #swaps casing for the string
print('Converts letter casing in \'%s\' to \'%s\'' % (rawstr,rawstr.upper()))

