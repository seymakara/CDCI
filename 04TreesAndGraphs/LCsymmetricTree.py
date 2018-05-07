#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            pair  = stack.pop(0)
            left = pair[0]
            right = pair[1]
            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val == right.val:
                stack.insert(0,[left.left, right.right])
                stack.insert(0,[left.right, right.left])
            else:
                return False
        return True