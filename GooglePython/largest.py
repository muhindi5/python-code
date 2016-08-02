#!/usr/bin/python3
def get_largest(nlist):
    largest = nlist[0]
    for num in range(1,len(nlist)):
        if largest < nlist[num]:
            largest = nlist[num]
            if num == len(nlist):
                break
    return largest
    
print(get_largest([32,4,22,7,1,119,9]))

def primer(val):
    if val%2 == 0:
        return False
    else:
        return True
while True:
    number = int(input('Is this number prime?'))
    print(primer(number))
