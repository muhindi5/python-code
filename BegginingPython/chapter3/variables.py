# Testing out variables
first_str = "This is the first"
second_str = "This is the second str"
third_str = "This is the third str"
#print the strings 
print("%s\n;%s\n:%s\n" % (first_str,second_str,third_str))

#Add number variables
num = 78
num2 = 23
print("%s\n%s\n%s\n%d\n%d\n" % (first_str,second_str,third_str,num,num2))

#using a turple for data storage
# turples are immutable 
#it references data such as strings and numbers inside a parenthesis
data = ("A Country for Old Men","J. Fox",39,"Penguin")
print("%s is a book authored by %s and published by %s. The price is USD%.2f " % (data[0],data[1],data[3],data[2]))
#to check number of items in the turple
print("Number of Items in Turple: %d" % len(data))

#reference a turple inside another
item_a = ("Book1","A.Bois",23)
item_b = (item_a,"Published: 2016","Penguin")
print(item_b)

#access specific item of turple inside other turple
print("The Author of the book is: %s " % item_b[0][1])

#Using Lists; are mutable
items = ["cofee","tea","cocoa","beer","vodka"]
print("Breakfast can be any of these beverages: %s" % items)
#change item 4 to 'soda'
items[3] = "Soda"
print("Breakfast has changes to be any of these beverages: %s" % items)
#Add an extra item to the end of the list
items.append("waffles")
print("Breakfast added: %s" % items[len(items)-1])

#Append more than 1 item to the list at once
items.extend(["oatmeal","eggs","toast"])
print("Now breakfast has: %s" % items)
# Total number of items
print("Total number of items in  breakfast: %d" % len(items))


