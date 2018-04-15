class Stack:
    def __init__(self):
         self.stack = []
    def push(self, item):
         self.stack.append(item)
    def pop(self):
         item = self.stack.pop()
         return item
    def isEmpty(self):
        return self.stack == []

class Solution(object):
    def isValid(self, s):
        stack = Stack()
        for i in range (len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.push(s[i])
            if s[i] == "]" or s[i] == ")" or s[i] == "}":
                if stack.isEmpty():
                    return False
                x = stack.pop()
                if s[i] == "]" and x != "[":
                    return False
                elif s[i] == ")" and x != "(":
                    return False
                elif s[i] == "}" and x != "{":
                    return False
        if stack.isEmpty() != True:
            return False
        return True