#!/usr/bin/python3

def selsort(ls):
   for fill_slot in range(len(ls)-1,0,-1):
      pos_of_max = 0
      for location in range(1,fill_slot+1):
         if ls[location] > ls[pos_of_max]:
            pos_of_max = location
      ls[fill_slot], ls[pos_of_max] = ls[pos_of_max],ls[fill_slot] #swap
      print('pass',fill_slot,ls)


values = [11,7,12,14,19,1,6,18,8,20]
print('Before',values)
selsort(values)
print('After',values)
