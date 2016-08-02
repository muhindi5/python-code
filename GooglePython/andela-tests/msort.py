#!/usr/bin/python3

def merge(left,right):
    merged = []
    leftIdx = rightIdx = 0
    while True:
        #right list exhausted
        if rightIdx >= len(right):
            return merged + left[leftIdx:]
        #left list exhausted
        elif leftIdx >= len(left):
            return merged + right[rightIdx:]
        #compare values in right and left indexes in both lists
        elif left[leftIdx] < right[rightIdx]:
            merged.append(left[leftIdx])
            leftIdx+=1
        else:
            merged.append(right[rightIdx])
            rightIdx +=1


def mergesort(ls):
    if len(ls) <= 1:
        return ls
    else:
        midIdx = int(len(ls)/2)
        left = mergesort(ls[:midIdx])
        right = mergesort(ls[midIdx:])
        return merge(left,right)

#test
numbers = [21,1,26,45,29,28,2,9,16,49,39,27,43,34,46,40]
print('Before',numbers)
mergesort(numbers)
print('After',numbers)



