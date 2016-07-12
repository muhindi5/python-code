# Using bubblesort

def bsort(items):
    for i in range(len(items)-1,0,-1):
#       print(i)
       for j in range(i):
 #       print(j)
        if items[j] > items[j+1]:
          items[j],items[j+1] = items[j+1],items[j] #swap now!

items = [23,45,76,12,34,14,67,33,25,41]
print(items)
bsort(items)
print(items)

