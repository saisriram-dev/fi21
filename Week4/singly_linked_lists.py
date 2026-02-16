# Singly linked lists in  python
""" A singly linked list is a linear data structure where elements are stored in nodes, 
    and each node points to the next node in the in the sequence using a single reference link.
    The last node in the list points to None, indicating the end of the list.
    Each node contains the data and a reference to the next node.
    The first node is called the head, and the last node is called the tail."""

# We build nodes using classes in python
class SinglyLinkedNode:
    def __init__(self, data, next_node=None): # By default next=None
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

# Defining the nodes of the linked list
Head = SinglyLinkedNode(1)
A = SinglyLinkedNode(2)
B = SinglyLinkedNode(3)
C = SinglyLinkedNode(7)

# Defining the links between the nodes
# Head -> A -> B -> C
Head.next_node = A
A.next_node = B 
B.next_node = C

# Traversing the linked list - O(n)
curr = Head
while curr is not None:
    print(curr)
    curr = curr.next_node

# Displaying the linked list - O(n)
def display_linked_list(head):
    curr = head
    elements = []
    while curr is not None:
        elements.append(str(curr.data))
        curr = curr.next_node
    return " -> ".join(elements)
print(f"The linked list is: {display_linked_list(Head)}")

# Search for node value in the linked list - O(n)
def search_linked_list(head, target):
    curr = head
    while curr is not None:
        if curr.data == target:
            return True
        curr = curr.next_node
    return False
print(f"Is 3 in the linked list? {search_linked_list(Head, 3)}")
print(f"Is 5 in the linked list? {search_linked_list(Head, 5)}")
