# Doubly Linked Lists in Python
"""Doubly linked lists are a type of linked list where each node contains a reference
to both the next and the previous node in the list.
This allows for efficient insertion and deletion of nodes from both ends of the list,
as well as traversal in both directions."""


class DoublyNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


# Demonstrating the creation of a doubly linked list with three nodes
Head = DoublyNode(1)
Second = DoublyNode(2)
Third = DoublyNode(3)

# Defining the links between the nodes
# It is in the form Head <-> Second <-> Third
Head.next = Second
Second.prev = Head
Second.next = Third
Third.prev = Second


# Traversing the list from head to tail
def traverse_forward(head):
    curr = head
    elements = []
    while curr is not None:
        elements.append(str(curr.value))
        curr = curr.next
    return " <-> ".join(elements)


print("Forward Traversal: ", traverse_forward(Head))


# Traversing the list from tail to head
def traverse_backward(tail):
    curr = tail
    elements = []
    while curr is not None:
        elements.append(str(curr.value))
        curr = curr.prev
    return " <-> ".join(elements)


print("Backward Traversal: ", traverse_backward(Third))


# Inserting a new node at the head of the list
def insert_at_head(head, value):
    new_node = DoublyNode(value)
    new_node.next = head
    if (
        head is not None
    ):  # If the list is not empty, set the previous pointer of the old head to the new node
        head.prev = new_node
    return new_node


# Inserting a new node at the tail of the list
def insert_at_tail(tail, value):
    new_node = DoublyNode(value)
    new_node.prev = tail
    if (
        tail is not None
    ):  # If the list is not empty, set the next pointer of the old tail to the new node
        tail.next = new_node
    return new_node


# Inserting at a specific position in the list (zero-indexed)
def insert_at_position(head, position, value):

    if position == 0:
        return insert_at_head(head, value)

    new_node = DoublyNode(value)

    curr = head
    for _ in range(position - 1):
        if curr is None:
            raise IndexError("Position out of bounds")
        curr = curr.next

    if curr is None:
        raise IndexError("Position out of bounds")

    # link new node
    new_node.next = curr.next
    new_node.prev = curr

    if curr.next is not None:
        curr.next.prev = new_node

    curr.next = new_node

    return head
