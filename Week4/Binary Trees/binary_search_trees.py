# Binary Search Tree implementation in Python
# In a binary search tree, for each node:
# - The left subtree contains only nodes with values less than the node's value.
# - The right subtree contains only nodes with values greater than the node's value.
# - Both the left and right subtrees must also be binary search trees.

#      5
#    /   \
#   1     8
#  / \    / \
# -1  3  7  9


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


# Constructing the binary search tree
A = TreeNode(5)
B = TreeNode(1)
C = TreeNode(8)
D = TreeNode(-1)
E = TreeNode(3)
F = TreeNode(7)
G = TreeNode(9)
A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G


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


# Function to search for a value in the binary search tree
# Time: O(log n) on average, O(n) in the worst case (if the tree is skewed)
def search_bst(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)


print(search_bst(A, 3))  # True
print(search_bst(A, 10))  # False
