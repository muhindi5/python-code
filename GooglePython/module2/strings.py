# using strings 

#printing a string 
str1 = 'sentence 1' 
str2 = 'sentence 2'
print(str1,str2)

#using a raw string literal...passes all string characters with no special treatment of backslash characters
raw_str = r'the \n character and the \t are special'
print(raw_str)
#represent a unicode string character
unistr = u'A Unicode string' #prefixed using 'u'
# convert a Unicode string to utf-8
unitstr.encode('utf-8')
print(unistr)
# convert back to unicode
unicode(unistr,'utf-8')

u_str = u'This is a Unicode string i.e 4 bytes are used to represent each character'
print(u_str)

#using methods on a string
phrase = 'marinated boogers are a delicacy in this country. Infact, I just has a plate of them'
print(phrase)
# change to upper case
print(phrase.upper())
#remove all white space at beggining and end
print(phrase.strip())
#spilt the phrase into tokens
tokens = phrase.split(' ')
print(tokens)
#using slices to represent sub-parts of a str

#find the occurance of a character and return index of first found
print(phrase.find('o'))

#replace words in a phrase 
print(phrase.replace('boogers','chicken'))

#using slices in a string 
# _str[start:end] returns all elements begining at the start and extending to but not including the end
mystr = 'hello'
print(mystr[1:3]) #'el'
print(mystr[-5:-1]) #negative indexes count from the end of the string # 'hell'
print(mystr[:]) # print a copy of the whole string by omitting all indices
print(mystr[3:]) #omitting either index defaults to start or end of string #'lo'


