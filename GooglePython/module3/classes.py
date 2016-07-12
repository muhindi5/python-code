# create class named Pet
class Pet:
    #attributes of pet instances
    alias = ''
    numberOfLegs = 0
    
    #methods of pet instances
    def sleep(self):
        print('sleeping...')

# instantiate an object from the class
mypet  = Pet()
mypet.alias = 'popi'
mypet.numberOfLegs = 2

#test the instance's props and methods
print('My pet named %s has %d legs' % (mypet.alias, mypet.numberOfLegs))
mypet.sleep()

