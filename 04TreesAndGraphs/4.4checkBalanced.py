 #Implement a function to check if a binary tree is balanced. For the purposes of this question, 
 # a balanced tree is de ned to be a tree such that the heights of the two subtrees of any node never differ by more than one.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def checkBalanced(self, root):
        if root == None:
            return 0
        leftHeight = self.checkBalanced(root.left)
        if leftHeight == -1:
            return -1
        
        rightHeight = self.checkBalanced(root.right)
        if rightHeight == -1:
            return -1
        
        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        return (1 + max(rightHeight, leftHeight))
    
    def isBalanced(self,root):
        if self.checkBalanced(root) > -1:
            return True 
        return False