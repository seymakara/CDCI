class Solution(object):
    
    def getLength(self, head): 
        if head == None:
            return 0
        
        length = 0
        current = head
        
        while current != None:
            length = length + 1
            current = current.next
        return length
    
    # def getTail(self, head): # not necessary
    #     if head == None:
    #         return None
        
    #     current = head
    #     while current.next != None:
    #         current = current.next
    #     return current
        
    def getIntersectionNode(self, headA, headB):
        
        if headA is None or headB is None:
            return None
        
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        
        
        longer = headA if lengthA >= lengthB else headB
        shorter = headB if lengthA >= lengthB else headA
        
        excess = abs(lengthA - lengthB)
        
        
        while excess > 0 and longer is not None:
            longer = longer.next
            excess -= 1
            
        while shorter is not None and shorter != longer:
            shorter = shorter.next
            longer = longer.next
        return shorter