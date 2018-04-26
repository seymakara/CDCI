class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, x):
        self.stack.append(x)
        if x<=self.getMin():
            self.minStack.append(x)
        

    def pop(self):
        poppedItem = self.stack.pop()
        if poppedItem == self.getMin():
            self.minStack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        if len(self.minStack)==0:
            return sys.maxsize
        else:
            return self.minStack[-1]