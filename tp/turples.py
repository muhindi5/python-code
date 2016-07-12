#!/usr/bin/python3
# working with turples

turple1  = ('Tariq','Hamza','Omar','Ramadhan')
turple2 = () #empty turplei
turple3 = (2,) #turple with 1 element, note the comma
turple4 = (34,54,23,65,12)

print(turple1)
print(turple2)
print(turple3)
print(turple4)

#access values in a turple
print(turple1[1:2]) #get element 1 to 2(exclusive)
print(turple4[-4:-2])

turple5 = turple1 + turple4
print(turple5)

#basic functions in turples
t1, t2, t3 = ('Red','Blue','Black'), ('Green','Yellow','Brown','Red'),(1,2,7)

#compare elements in turples
print(t1,t2) #longer turple is larger
print(t2,t3)  #if either element is a number, other element is larger

print('Smallest item in \'%s\': %s' % (t2,min(t2)))
