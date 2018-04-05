class Stack:
    def __init__(self, capacity):
        self.stacks = []
        if capacity < 1:
             raise NameError("Stack height cannot be 0")
        else: self.capacity = capacity
    def push(self, item):
        if len(self.stacks) == 0:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)
    def pop(self):
        if len(self.stacks) == 0:
            raise NameError("Stack is empty")
        else:
            itemToBePopped = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
        return itemToBePopped

newStack = Stack(2)
newStack.push(1)
newStack.push(1)
newStack.push(2)
# newStack.push(2)
newStack.pop()
print len(newStack.stacks)
print newStack.stacks
print newStack.stacks[-1]