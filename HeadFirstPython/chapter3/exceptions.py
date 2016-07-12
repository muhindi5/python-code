#Open a text file,for every line in file split at the ':' character, print-out the line after adding a sting 'says'
#throw appropriate exceptions if the file is missing or a line that cannot be split is encounted

try:
    datafile = open('talk.txt') 
    for each_line in datafile:
        #split each line on the ':' character
        try:
            (actor,role) = each_line.split(':')
            print(actor,end='')
            print(' says: ',end='')
            print(role,end='')
        except ValueError:
            pass
    datafile.close()
except IOError:
    print('The datafile is missing')



