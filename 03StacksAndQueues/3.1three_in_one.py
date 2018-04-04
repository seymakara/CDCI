class FixedMultiStack:

    def __init__(self, stacksize):
        self.numberOfstacks = 3
        self.values = [0] * (stacksize * self.numberOfstacks)
        self.sizes = [0] * self.numberOfstacks
        self.stacksize = stacksize

    def Push(self, item, stackNumber):
        if self.IsFull(stackNumber):
            raise Exception('Stack is full')
        self.sizes[stackNumber] += 1
        self.values[self.IndexOfTop(stackNumber)] = item

    def Pop(self, stackNumber):
        if self.IsEmpty(stackNumber):
            raise Exception('Stack is empty')
        valueTobePopped = self.values[self.IndexOfTop(stackNumber)]
        self.values[self.IndexOfTop(stackNumber)] = 0
        self.sizes[stackNumber] -= 1
        return valueTobePopped

    def Peek(self, stackNumber):
        if self.IsEmpty(stackNumber):
            raise Exception('Stack is empty')
        return self.values[self.IndexOfTop(stackNumber)]

    def IsEmpty(self, stackNumber):
        return self.sizes[stackNumber] == 0

    def IsFull(self, stackNumber):
        return self.sizes[stackNumber] == self.stacksize

    def IndexOfTop(self, stackNumber):
        offset = stackNumber * self.stacksize
        return offset + self.sizes[stackNumber] - 1


def ThreeInOne():
    newstack = FixedMultiStack(2)
    print newstack.IsEmpty(0)
    newstack.Push(3, 0)
    newstack.Push(2, 0)
    print newstack.Peek(0)
    print newstack.IsEmpty(1)
    print "index", newstack.IndexOfTop(0)
    # print newstack.Pop(0)
    # print newstack.Peek(1)
    newstack.Push(3, 1)

ThreeInOne()
