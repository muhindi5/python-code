#!/usr/bin/python3
class Queue(object):
    '''implemeting a queue from 2 stacks'''
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self,item):
        return self.in_stack.append(item)
    
    #move last item in_stack to out_stack
    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop()
        while self.in_stack:
            self.out_stack.append(self.in_stack.append(item))
        if not self.out_stack:
            raise Exception('Queue is empty')
        return self.out_stack.pop()
    
    #return size of both stacks
    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    #get last item in the list:w

    def peek(self):
        if self.out_stack:
            return self.out_stack[-1]
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.iout_stack[-1]
        else:
            return None

def main():
    queue = Queue()
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)
    print(queue.size())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
if __name__ == '__main__':
    main()
