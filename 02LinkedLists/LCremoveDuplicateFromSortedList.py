#Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        while curr:
            while curr.next is not None and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head