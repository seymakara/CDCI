class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next=self.head
        self.head = node

    def insertEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def getList(self):
        current  = self.head
        while current:
            print current.data 
            current= current.next

#   have two runners fast and slow, and an empty stack
#   while fast and fast.next exist move them (slow one node, fast two nodes)
#   push the slow data into stack
#   check if list has odd number of elements (fast becomes null if it is even), if so:
        #   slow = slow.next 
#   pop out the top element from stack and check if it is same with slow data

    def isPalindrome(self):
        fast = self.head
        slow = self.head
        stack  = []

        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next
        
        if fast is not None:
            slow = slow.next #(skips the middle node, when the list has odd number of nodes)
        
        while slow:
            top = stack.pop()

            if top != slow.data:
                return False
            slow = slow.next
        return True

ll_true = LinkedList()
ll_true.insertEnd(1)
ll_true.insertEnd(2)
ll_true.insertEnd(3)
ll_true.insertEnd(4)
ll_true.insertEnd(3)
ll_true.insertEnd(2)
ll_true.insertEnd(1)
ll_true.insertEnd(2)
print ll_true.isPalindrome()