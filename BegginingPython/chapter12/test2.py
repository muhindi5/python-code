#!/usr/bin/python3

import unittest

class ArithTestSuper(unittest.TestCase):
	def setup(self):
		print('Setting up ArithTest cases')
	def tearDown(self):
		print('cleaning up test cases')

class ArithTest(ArithTestSuper):
	def runTest(self):
		'''Test addition and succeed'''
		print('runnning arithtest')
		self.failUnless(1+1==2,'test1 unless equals')
		self.failIf(1+1!=2,'test2: has to equal')
		self.failUnlessEqual(1+1,2,'test3: unless equal to')

class ArithTestFail(ArithTestSuper):
	def runTest(self):
		'''Test addition and fail'''
		print('runnning arithtestfail')
		self.failUnless(1+1==3,'test1 unless equals')
		self.failIf(1+1!=5,'test2: has to equal')
		self.failUnlessEqual(1+1,2,'test3: unless equal to')

class ArithTest2(ArithTestSuper):
	def setup(self):
		print('setting up ArithTest2 classes')
	def teardown(self):
		print('tearing down ArithTest2 classes')
	def runArithTest(self):
		'''test addition and succeed in one class'''
		print('running ArithTest in ArithTest2')
		self.failUnless(1+1==3,'test1 unless equals')
		self.failIf(1+1!=5,'test2: has to equal')
		self.failUnlessEqual(1+1,2,'test3: unless equal to')

def suite():
	suite = unittest.TestSuite()
	#First style
	suite.addTest(ArithTest())
	suite.addTest(ArithTestFail())
	#style 2
	suite.addTest(ArithTest2('runArithTest'))
#	suite.addTest(ArithTest2('runArithTestFail'))
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	tsuite = suite()
	runner.run(tsuite)


		



