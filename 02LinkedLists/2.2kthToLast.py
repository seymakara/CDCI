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
    
    # return  none if the list is empty
    # have two runners at the head
    # place them k nodes apart by moving fast one k nodes.
    # move them at the same pace.
    # when fast one hits the end slow one will be at the kth node.

    def kthToLast(self, k):

        if self.head == None:
            return None 

        else:

            r1 = self.head
            r2 = self.head
            
            if k == 0:
                k += 1

            for i in range (k):
                r1 = r1.next

            while r1:
                r1 = r1.next
                r2 = r2.next

        return r2.data

l = LinkedList()
l.insertEnd(8)
l.insertEnd(5)
l.insertEnd(2)
l.insertEnd(3)
l.insertEnd(11)
l.insertEnd(1)
l.insertEnd(7)
l.insertEnd(16)

l.getList()
print "==========="
print l.kthToLast(0)

