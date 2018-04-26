# Write an algorithm to  nd the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
#You may assume that each node has a link to its parent.

class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k

def inorderSuccessor(root, X):
    if X == None:
        return None
    if X.right is not None:
        return leftMostChild(X.right)
        
    #Start from root and search for successor down the tree
    succ = None
    while root is not None:
        if (X.data < root.data):
            succ = root
            root = root.left
        elif (X.data > root.data):
            root = root.right
        return succ
       
def leftMostChild(n):
    if n == None:
        return None
    while n.left != None:
        n = n.left
    return n
