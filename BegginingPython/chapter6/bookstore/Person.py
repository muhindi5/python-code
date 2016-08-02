#!/usr/bin/python3

class Person:
    '''Base class models common behavior and attribs of all users'''
    #class variable for instance count
    person_count = 0
    def __init__(self,f_name,l_name,id_,email_addr):
        self.f_name = f_name
        self.l_name = l_name
        self._id = _id
        self.email_addr = email_addr
        person_count +=1
        
    #will be called when del is used on instance
    def __del__(self):
        print('Deleting instance')
    #set attributes 
    def set_fname(self,name):
        self.f_name = name
        print('calling parent method')
    def login(self):
        print('User logged in')
    def get_objstr(self):
        print('object string: %s ' % str(self))

#define a child class
class Manager(Person):
    mcount= 0
    def __init__(self):
        print('calling child constructor')
        Manager.mcount+=1
    def approve(self):
        print('Called approve method')
    #override login method in Person
    def login(self):
        print('manager logged in')

#Test methods 
user = Manager()
user2 = Manager()
user.approve()
user.set_fname('Bodu')
user.login()
user.get_objstr()
print('Count of Person instances: %d ' % Manager.mcount)
#check if instance is subclass of Person
print('\'Manager\' --> subclass of \'Person\': %s' % issubclass(Manager,Person))
