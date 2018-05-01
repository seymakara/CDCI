# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            curr = head # current i head e esitle
            head = head.next # head i bir ileriye tasi
            curr.next = prev #current in yonunu geriye cevir
            prev = curr # gerideki node u current a esitle (current ve node ayni yerde)
        return prev

# RECURSIVE SOLUTION

    # def reverseList(self, head):
    #     return self._reverse(head)

    # def _reverse(self, node, prev=None):
    #     if not node:
    #         return prev
    #     n = node.next
    #     node.next = prev
    #     return self._reverse(n, node)