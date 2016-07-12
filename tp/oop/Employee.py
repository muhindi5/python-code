#!/usr/bin/python3

class Employee:
    '''Common base class for all employees'''
    
    empCount = 0 #class variable
    
    #constructor: called when 
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
    
    #get total number of employees    
    def displayCount(self):
        print('Total Employee %d '% Employee.empCount)
    
    #print details of the employee
    def displayEmployee(self):
        print('Name: %s, Salary: %s' % (self.name,self.salary))

#create instances of the class
emp1 = Employee('Dinar',45000.00)
emp2 = Employee('Allexi',32000.00)

#display the employees
emp1.displayEmployee()
emp2.displayEmployee()

#print number of employees
emp1.displayCount()

#using object functions 
print(getattr(emp1,'salary')) #get attribute 'salary'
setattr(emp1,'name','Popi') #set attribute name to 'Popi' 
emp1.displayEmployee()
print('emp1 has attribute \'name\': %s' % hasattr(emp1,'age')) #check if object has specified attribute

#built-in class methods
print(emp1.__dict__) #display dictionary containing class's namespace
print(emp1.__doc__) #class documentation string, none if undefined
#print(emp1.__name__) #class name:
print(emp1.__module__) #module inwhich the class is defined

#destroying objects (grabage collection)
#Python's gc is automatically triggered when an object's reference count reaches 0
# a class can create an explicit destructor invoked when the  instance is about to be destroyed

print('**********************************************************')
class Point:
 
    def __init__(self,x= 0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print('About to kill --> %s' % class_name)

#create instance of Point
p1 = Point()
p2 = p1
print('Object Id \'p1\': %d '% id(p1))
print('Object Id \'p2\': %d '% id(p2))
del p1

print('')
