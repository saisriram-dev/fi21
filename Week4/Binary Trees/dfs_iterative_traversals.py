# Binary trees

"""Example Tree:
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


# Function to perform pre-order traversal of the tree
def pre_order_traversal(node):
    stk = []

    if node:
        stk.append(node)

    while stk:
        current = stk.pop()
        print(current.val)  # Process the current node

        # Push right child first so that left child is processed first
        if current.right:
            stk.append(current.right)
        if current.left:
            stk.append(current.left)


pre_order_traversal(A)


# Function to perform in-order traversal of the tree
def in_order_traversal(node):
    stk = []
    current = node

    while stk or current:
        while current:
            stk.append(current)
            current = current.left

        current = stk.pop()
        print(current.val)  # Process the current node
        current = current.right


in_order_traversal(A)


# Function to perform post-order traversal of the tree
def post_order_traversal(node):
    stk = []
    last_visited = None
    current = node

    while stk or current:
        while current:
            stk.append(current)
            current = current.left

        peek_node = stk[-1]

        # If right child exists and traversing node from left child, then move right
        if peek_node.right and last_visited != peek_node.right:
            current = peek_node.right
        else:
            print(peek_node.val)  # Process the current node
            last_visited = stk.pop()


post_order_traversal(A)
