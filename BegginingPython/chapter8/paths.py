#!/usr/bin/python3
import os

def split(path):
    '''recursively split a path's directories into a turple'''
    #return turple with parent dir and last path component
    parentdir,name = os.path.split(path)
    print(parentdir)
    if name == "": #when split() cant split a path any further
        return (parentdir,)
    else:
	    return split(parentdir) + (name,)

def getext(fname):
	'''get the extension of a specified file'''
	parts = os.path.splitext(fname)
	return parts[1]


def getfiles(path):
	'''list contents of a directory using full path'''
	for name in os.listdir(path):
		print(os.path.join(path,name)) #join path and dir item


def print_tree(path):
	'''recursively traverse path and any subdirs inside'''
	for name in os.listdir(path):
		full_path = os.path.join(path,name)
		print(full_path)
		if os.path.isdir(full_path):
			print_tree(full_path)



path = '/home/kelli/glassfish4/glassfish/bin'
file1 = path+'/capture_schema'
print(split(path))
print('file extension-->%s' % getext(file1))
print('file absolute path:',os.path.abspath(file1)) #get absolute path from relative
print('directory\'',file1,'\' exists?',os.path.exists(path)) #check if directory exists
print('Items in dir',os.listdir(path)) #get contents of a directory
print('Listing in directory',getfiles(path))
#print('items in dir:',print_tree('/home/kelli'))
print('creating directory...',os.mkdir('/home/kelli/ptest'))
os.rmdir('/home/kelli/ptest')

import glob
print(glob.glob('/home/kelli/*.txt'))
