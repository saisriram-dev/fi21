# Binary trees

""" Example Tree:
        A=1
    B=2       C=3
D=4       E=5       F=10 (5 is related to 2 not 3)
"""

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
