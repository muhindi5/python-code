#!/usr/bin/python

import unittest

class ArithTest (unittest.TestCase):
    def runTest(self):
        '''Test addition '''
        self.failUnless(1+1==2,'one plus one fails')
        self.failIf(1+1!=2,'one plus one fails again')
        self.failUnlessEqual(1+1,2,'more trouble with one plus one')

    
class ArithTestFail(unittest.TestCase):
    '''ArithTestFail implementation'''
    def runTest(self):
        '''Test addition and fail'''
        self.failUnless(1+1==3,'Expected this to fail')
        self.failIf(1+1!=5,'This too would fail')            

def create_suite():
        suite = unittest.TestSuite()
        suite.addTest(ArithTest())
        suite.addTest(ArithTestFail())
        return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    testSuite = create_suite()
    runner.run(testSuite)



