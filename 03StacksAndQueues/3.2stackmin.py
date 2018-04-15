import sys
class Stack:
     def __init__(self):
         self.stack = []
         self.minStack = []

     def isEmpty(self):
         return self.stack == []

     def push(self, item):
         self.stack.append(item)
         if item <= self.min() or len(self.minStack) == 0:
             self.minStack.append(item)

     def pop(self):
         item = self.stack.pop()
         if item == self.min():
             self.minStack.pop()
         return item

     def size(self):
         return len(self.stack)
    
     def min(self):
        if len(self.minStack) == 0:
            return sys.maxsize
        else :
            return self.minStack[-1]

print "Push elements to the stack"
newStack = Stack()
newStack.push(3)
newStack.push(2)
newStack.push(5)
newStack.push(1)
# newStack.push(7)
newStack.pop()
print newStack.stack
print newStack.minStack
print newStack.min()

