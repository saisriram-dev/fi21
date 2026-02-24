# Binary trees

""" Example Tree:
        A=1
    B=2       C=3
D=4       E=5       F=10 (5 is related to 2 not 3)
"""
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)

# Creating the tree nodes
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

# Building the tree structure
A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

def search_tree(node, target):
    if node is None:
        return False
    
    if node.val == target:
        return True
    
    return search_tree(node.left, target) or search_tree(node.right, target)

search_tree(A, 5)  # True
search_tree(A, 10) # True
search_tree(A, 7)  # False
