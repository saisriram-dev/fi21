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

# Function to perform in-order traversal of the tree. Time complexity: O(n), Space complexity: O(h) where h is the height of the tree
def pre_order_traversal(node):
    if not node:
        return []
    
    print(node)  # Print the current node value
    pre_order_traversal(node.left)  # Traverse left subtree
    pre_order_traversal(node.right)  # Traverse right subtree

pre_order_traversal(A)  

# Function to perform in-order traversal of the tree. Time complexity: O(n), Space complexity: O(h) where h is the height of the tree
def in_order_traversal(node):
    if not node:
        return []

    in_order_traversal(node.left)  # Traverse left subtree
    print(node)  # Print the current node value
    in_order_traversal(node.right) # Traverse right subtree

in_order_traversal(A) 

# Function to perform post-order traversal of the tree. Time complexity: O(n), Space complexity: O(h) where h is the height of the tree
def post_order_traversal(node):
    if not node:
        return []

    post_order_traversal(node.left)  # Traverse left subtree
    post_order_traversal(node.right) # Traverse right subtree
    print(node)  # Print the current node value

post_order_traversal(A)
