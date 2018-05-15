# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

class MyStack(object):

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        q = self.queue # NEDEN YENI BIR QUEUE YA EKLIYORUZ?
        q.append(x)
        
    def pop(self):
        return self.queue.pop()
        

    def top(self):
        return self.queue[-1]
        

    def empty(self):
        return len(self.queue) == 0

    # def empty(self): WHY NOT THIS WORKS
    #     return self.queue == []