#create oldStack and newStack
#push new item into new stack
#check if oldstack is empty
    #if so while newStack is not empty
        # oldStack.push(newStack.pop())
#for peek:
    #shift stacks
    # return oldestStack peek
#for remove:
    #shift stacks
    # return oldestStack pop

class myQueue():
    oldStack = []
    newStack = []

    def add(self,item):
        self.newStack.append(item)

    def shiftStacks(self):
        if len(self.oldStack) == 0:
            while self.newStack:
                self.oldStack.append(self.newStack.pop())
    def peek(self):
        self.shiftStacks()
        return self.oldStack[-1]

    def remove(self):
        self.shiftStacks()
        return self.oldStack.pop()

newQueue = myQueue()

newQueue.add(1)
newQueue.add(2)
newQueue.add(3)
print newQueue.newStack
print newQueue.peek()
print newQueue.newStack
print newQueue.remove()
print newQueue.oldStack

