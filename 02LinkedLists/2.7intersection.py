class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.size = 1
        self.tail = None

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

    def returnHead(self):
        return self.head

    def getTailandSize(self):
        size = self.size
        tail = self.tail
        current = self.head
        if self.head == None:
            return None
        while current.next is not None:
            size += 1
            current = current.next
            
        return size
        tail = current
        return tail
    
    def getKthNode(self, k):
        current = self.head
        while k > 0 and current is not None:
            current = current.next
            k -= 1
        return current

def findIntersection(list1, list2):
    if list1 is None or list2 is None:
        return None
    
    result1 = getTailandSize(list1)
    result2 = getTailandSize(list2)

    if result1.tail != result2.tail:
        return Null

    else:
        longer  = list1 if list1.size > list2.size else list2
        shorter = list2 if list1.size > list2.size else list1

        longer = getKthNode(longer, abs(result1.size - result2.size)) # to chop of the the excess nodes in longer one

        while shorter != longer:
            shorter = shorter.next
            longer = longer.next
        return shorter # return either one



