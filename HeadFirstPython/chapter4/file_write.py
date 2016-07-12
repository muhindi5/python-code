# Writting to a file

import os
try:
    out = open("file4.out")
    print("This file can be written to...",file=out)
    #Flush the buffer
    out.close()
except IOError as err:
    print('File IO Error' + str(err))
finally:
    #check if the 'out' object was created...
    if 'out' in locals():
        out.close()

#Python provides the use of the 'with' construct that enables us avoid using the finally construct

try:
    with open('file5.out','w') as fileobj:
        print('Printed to the file')
except IOError:
    print('A file error occured')



