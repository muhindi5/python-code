#!/usr/bin/python3
# Topic #3:Introduction

#new-line characters
s = 'c:\\My Documents\netbooks'
rstr = r'c:\\My Documents\netbooks'
print(s) #will be printed including new line
print(rstr) #raw string as-iis

#long strings
text = ('This is a long string that needs to be broken into 2 lines for'
'readability. Without the closing brackets, Python would see this as'
' 2 separate statements')
print(text)

#subscripting strings
words = 'Greenland'
print(words[0])
print(words[4])
print(words[-3]) #print from the last index
#nb: start is always included, end is always excluded, this makes sure that s[:i] + s[i:] = s
print(words[:2] + words[2:]) #an ommited first index defaults to 0 and an ommitted last index defaults to size of the string being split

#replace characters of a string
print('Por' + words[2:])


#print Fibonacci series
a,b = 0,1
while b < 10:
    print(b)
    a,b = b,a+b

