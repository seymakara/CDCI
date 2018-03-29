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
    
    def findNode(self, k):
        if self.head == None:
            return None
        
        current = self.head
        while current:
            if current.data == k:
                return current
            current = current.next

        
    def deleteMiddleNode(self, node):

        if node == None or node.next == None:
            return False
        
        next = node.next
        node.data = next.data
        node.next = next.next
        return True
    
l = LinkedList()
l.insertEnd(8)
l.insertEnd(5)
l.insertEnd(2)
l.insertEnd(3)
l.insertEnd(11)
l.insertEnd(1)
l.insertEnd(7)
l.insertEnd(16)

node = l.findNode(7)
print "*********"
l.getList()
l.deleteMiddleNode(node)
print "+++++++++"
l.getList()
