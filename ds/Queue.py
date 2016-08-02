#!/usr/bin/python3

#Implementation of a queue using a list

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    #insert will be Olog(n)
    def enqueue(self,item):
        self.items.insert(0,item)
    #remove from queue Olog(1)
    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

#test the queue
mq = Queue()
mq.enqueue(67)
mq.enqueue('Tommy')
mq.enqueue(False)
mq.dequeue()
print(mq.size())


