# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# For example:
# Given BST [1,null,2,2],
#    1
#     \
#      2
#     /
#    2
# return [2].

# Note: If a tree has more than one mode, you can return them in any order.

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        count = {}
        self.dfs(root, count)
        
        res = []
        if count != {}: # covers the case of an empty node
            max_count = max(count.itervalues())
            for key, value in count.iteritems():
                if value == max_count:
                    res.append(key)
        return res
            

    def dfs(self, node, count): # counts the nodes and put nodes and their values(how many) in dictionary
        if node:
            count[node.val] = count.get(node.val, 0) + 1 # .get() either brings you the value of the key in a dict or assigns 0 (if there is no such key). This is a shortcut to add a key and value in a dictionary.
            self.dfs(node.left, count)
            self.dfs(node.right, count)