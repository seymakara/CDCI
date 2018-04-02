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

    def returnHead(self):
        return self.head

# THE FUNCTION SUMLINKEDLISTS DOES NOT BELONG TO LINKEDLIST CLASS!
# Iki linked list i topla, yeni bir linked list olustur. yeni olusturdugun linked list in head ini dondur

    # 10 a bolumunden kalan bolumu carry variable ina koy
    # 10 a bolumunden kalani sum a koy
    # node = Node(sum+carry)
    # node1 = node1.next
    # node2 = node2.next
    # node.next = sumLinkedLists(node1, node2, carry) // bu geriye dogru bir sekilde hesaplayip, toplam linkedlistinin head ini donduruyo
    # return node

def sumLinkedLists(node1, node2, carry = 0):

    if node1 == None and node2 == None:
        return None

    total = carry
    if node1 != None:
        total += node1.data
    if node2 != None:
        total += node2.data

    node = Node(total%10)
    carry = int(total) / 10
    
    if node1:
        node1 = node1.next
    if node2:
        node2 = node2.next

    node.next = sumLinkedLists(node1, node2, carry)
    return node

# represents 1617
l1 = LinkedList()
l1.insertEnd(7)
l1.insertEnd(1)
l1.insertEnd(6)
l1.insertEnd(1)
l1.getList()
l1Head = l1.returnHead()

# represents 295
l2 = LinkedList()
l2.insertEnd(5)
l2.insertEnd(9)
l2.insertEnd(2)
l2.getList()
l2Head = l2.returnHead()

totalHead = sumLinkedLists(l1Head, l2Head)
while totalHead != None:
    print totalHead.data
    totalHead = totalHead.next