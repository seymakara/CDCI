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

    def delete(self, data):
        if self.head == None:
            print "head none" 
            return None
        else:
            current = self.head
            prev = None
            
            while current is not None:
                if current.data == data:
                    if prev == None: #this shows that we are at the head.
                        self.head = current.next
                    else: #this means that prev is not empty and we are not at the head position
                        prev.next = current.next # because prev is following (one step behind) current
                prev = current
                current = current.next

            return False

    # def removeDups(self):
    #     current = second = self.head 

    #     while current is not None:
    #         while second.next is not None:
    #             if second.next.data == current.data:
    #                 second.next = second.next.next
    #             else:
    #                 second = second.next
    #         second = current.next
    #         current = current.next
    
    def removedupsHash(self): # removing duplicates using hashtable
        newDict = {}
        current = self.head
        prev = None

        while current is not None:
            if current.data in newDict:
                prev.next = current.next
                current = current.next #prec should stay same otherwise current and prev moves to the same spot
            else:
                newDict[current.data] = 1
                prev = current
                current = current.next

l = LinkedList()
l.insertEnd(15)
l.insertEnd(13)
l.insertEnd(13)
l.insertEnd(15)
l.insertEnd(15)
l.insertEnd(13)
l.insertEnd(15)
l.insertEnd(18)
# l.delete(15)
l.getList()
l.removedupsHash()
print "=============="
l.getList()
