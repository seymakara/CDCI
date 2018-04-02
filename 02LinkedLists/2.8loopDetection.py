def loopDetection(self):
    fast = self.head
    slow = self.head

    while fast != None and fast.next != None: #checks if a loop exists in the list
        slow = slow.next
        fast = fast.next
        if slow == fast:
            break

    if fast == None or fast.next == None:
        return None
    
    slow = self.head # when they collide, both collision point and head are at the same nodes away from the start of the loop.
    while slow != None:
        slow = slow.next
        fast = fast.next
    
    return fast