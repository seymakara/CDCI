class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
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
    
    def findNode(self, k):
        if self.head == None:
            return None
        
        current = self.head
        while current:
            if current.data == k:
                return current
            current = current.next

    def partition(self, k):
        leftHead = None
        leftEnd = None
        rightHead = None
        rightEnd = None
        current = self.head

        while current is not None:
            if current.data < k:
                if leftHead == None:
                    leftHead = current
                    leftEnd = current
                else:
                    leftEnd.next = current
                    leftEnd = leftEnd.next

            else:
                if rightHead == None:
                    rightHead = current
                    rightEnd = current
                else:
                    rightEnd.next = current
                    rightEnd = rightEnd.next
            current = current.next
        leftEnd.next = rightHead
        rightEnd.next = None
        self.head = leftHead
        

l = LinkedList()
l.insertEnd(8)
l.insertEnd(5)
l.insertEnd(2)
l.insertEnd(3)
l.insertEnd(11)
l.insertEnd(1)
l.getList()
print "*********"
l.partition(5)
l.getList()


