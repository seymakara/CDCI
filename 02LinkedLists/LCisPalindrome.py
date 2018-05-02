#Given a singly linked list, determine if it is a palindrome.

class Solution(object):
    # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        stack = []
        fast = head
        slow = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast is not None: # this means that you list length is not even. [1,2,3,2,1]
            slow = slow.next # so you skip the middle item, because it is unique.
        while slow:
            popped = stack.pop()
            if popped != slow.val:
                return False
            slow = slow.next
        return True
