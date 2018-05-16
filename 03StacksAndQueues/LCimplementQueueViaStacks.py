class MyQueue(object):
    def __init__(self):           
        self.oldStack = []
        self.newStack = []
        
    def push(self, x):
        self.newStack.append(x)
        
    def shiftStacks(self):
        if len(self.oldStack) == 0:
            while self.newStack:
                self.oldStack.append(self.newStack.pop())

    def pop(self):
        self.shiftStacks()
        return self.oldStack.pop()
        

    def peek(self):
        self.shiftStacks()
        return self.oldStack[-1]
        

    def empty(self):
        if len(self.newStack) == 0 and len(self.oldStack) == 0:
            return True
        else:
            return False

class MyQueue2(object):
    def __init__(self):           
        self.newStack = []
        
    def push(self, x):
        self.newStack.append(x)

    def pop(self):
        return self.newStack.pop(0)
        

    def peek(self):
        return self.newStack[0]
        

    def empty(self):
        if len(self.newStack) == 0:
            return True
        else:
            return False