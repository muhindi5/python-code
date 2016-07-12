#Create empty lists and populate them using data from the file.
man = []
other = []

try:
    datafile = open('talk.txt') 
    for each_line in datafile:
        try:
            (role,line_spoken) = each_line.split(':',1)
            #remove whitespace from the string
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'OtherMan':
                other.append(line_spoken)
        except ValueError:
            pass
    datafile.close()
except IOError:
    print('The datafile is missing')
    
print(man)
print(other)



