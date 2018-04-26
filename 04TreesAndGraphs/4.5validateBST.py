# Implement a function to check if a binary tree is a binary search tree.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.checkBST(root, None, None)
    
    def checkBST(self, root, min, max):
        if root == None:
            return True
        if (min != None and root.val <= min) or (max != None and root.val >= max): # if min or max is None, it means it is the begining, passes this part and updates min and max.
            return False
        if self.checkBST(root.left, min, root.val) == False or self.checkBST(root.right, root.val, max) == False: #updates min and max and checks if they validate the rule of BST (left should be smaller, vice versa)
            return False
        return True