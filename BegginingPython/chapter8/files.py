#!/usr/bin/python3

import os

def create_file():
    ''' create a text file and write content into it'''
    f_obj = open('test.txt','w')
    f_obj.write('This is how to create a text file')
    f_obj.close()

def create_file2(file_name,flag,content):
    ''' create file based on specified params
        notes on flags:
        a - appends to a file
        w - writes to a file, deletes an existing file and creates new one.
        r - read from file (is the default falg if any is ommited)
        '''

    if os.path.isfile(file_name):
        print('File already exists, appending content')
        #fobj.write(content)
    else:
        fobj = open(file_name,flag)
        fobj.write(content)
        fobj.close()
        del fobj #delete the object 

def read_file(file_name):
    fobj = open(file_name,'r')
    print(fobj.read()) #readline gets one line at a time, read gets all content


def getline_len(fname):
    '''get the length of lines in a text file'''
    fob = open(fname,'r')
    lines = fob.readlines()
    for x in lines:
        print (len(x))

def path_test(fname):
    '''gets the parent and file dir'''
    parentdir, name = os.path.split(fname) #returns turple with the 2 items
    print('parent directory ==>',parentdir)
    print('file directory ==>',name)


def main():
    str1 = '''Created by Heisenberg\ncopyright 2016\n=============================\nInstallation guide:\n=============================='''
    str2 = '2016-2018'
    str3 = '/home/kelli/ftest'
    #create_file()
    create_file2(str3,'w',str1)
    #create_file2('/home/kelli/test1.txt','a',str2)
    read_file(str3)# read content of created file
    getline_len(str3)
    #path_test(str3)
    print(getdirs(str3))
if __name__ == '__main__':
    main()


