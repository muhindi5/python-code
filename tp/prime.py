#!/usr/bin/python3

def getPrimes(value):
    pnumbers  = []
    for i in range(1,value):
        if (i%1 == 0) and (i%i == 0 ):
            pnumbers.append(i)
    return pnumbers
 
def getExponent(val,start,end):
    for x in range(start,end):
        print(val**x)

#print('Getting all primes btwn 0 and %d' % 20000)
#results = getPrimes(20000)
#for current in results:
#    print (current)
getExponent(40,0,300)



