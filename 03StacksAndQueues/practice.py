class fixedMultiStack:
    def __init__(self, stacksize):
        self.numberOfstacks = 3
        self.values = [0] * (self.numberOfstacks * stacksize)
        self.sizes = [0] * self.numberOfstacks
        self.stacksize = stacksize

    def push(self, item, stackNumber):
        if self.isFull(stackNumber):
            raise Exception("Stack is Full")
        self.sizes[stackNumber] += 1
        self.values[self.indexofTop(stackNumber)] = item
        values = self.values
        print "values", values

    def pop(self, stackNumber):
        if self.isEmpty(stackNumber):
            raise Exception("Stack is Empty")
        self.values[self.indexofTop(stackNumber)] = 0
        self.sizes[stackNumber] -= 1
    
    def peek(self, stackNumber):
        if self.isEmpty(stackNumber):
            raise Exception("Stack is Empty")
        return self.values[self.indexofTop(stackNumber)]

    def isFull(self, stackNumber):
        if self.sizes[stackNumber] == self.stacksize:
            return True

    def isEmpty(self, stackNumber):
        if self.sizes[stackNumber] == 0:
            return True

    def indexofTop(self, stackNumber):
        offset = stackNumber * self.stacksize
        return offset + self.sizes[stackNumber] -1

def threeinOne():
    newstack = fixedMultiStack(2)
    newstack.push(1,0)
    newstack.push(2,0)
    newstack.push(3,1)
    newstack.push(4,1)
    newstack.push(5,2)
    newstack.push(6,2)

threeinOne()