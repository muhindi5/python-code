# find the largest number in a list 

def get_largest(x,n):
    for current in x:
        if current >= n:
            n = current
    return n

x = [34,56,12,67,344,893,15]
print('The largest number in %s is %d' % (x,get_largest(x,0)))

