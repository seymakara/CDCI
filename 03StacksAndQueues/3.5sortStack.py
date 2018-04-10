class sortStack():
    def __init__(self):
         self.stack = []
         self.newStack = []
    def add(self, item):
        self.stack.append(item)
    def peek(self):
        return self.stack[-1]
    def sort(self):
        while len(self.stack) > 0:
            temp = self.stack.pop()
            print "temp", temp
            while len(self.newStack) > 0  and self.newStack[-1] > temp:
                self.stack.append(self.newStack.pop())
            self.newStack.append(temp)
            print "peek", self.newStack[-1]
            print "newstack", self.newStack
        while len(self.newStack) > 0:
            self.stack.append(self.newStack.pop())

newStck = sortStack()

newStck.add(7)
newStck.add(10)
newStck.add(5)

print newStck.stack
print newStck.sort()
print "sorted", newStck.stack
print newStck.peek()





