# Queues in python
# A queue is a data structure that follows the First In First Out (FIFO) principle.
# We mainly use Doubly linked lists to implement queues in python

"""| Operation    | list     | deque    | 
   | ------------ | ------   | ------   |
   | append right | O(1)     | O(1)     |
   | pop right    | O(1)     | O(1)     |
   | append left  | ❌ O(n)  | ✅ O(1) |
   | pop left     | ❌ O(n)  | ✅ O(1) |
"""
# deque is a double-ended queue that allows us to add and remove elements from both ends efficiently.
# We can use a deque to implement a queue in Python
from collections import deque

# Create a queue
queue = deque()

# Adding elements to the queue - O(1)
queue.append(1)
queue.append(2)
queue.append(3)

# Removing elements from the queue - O(1)
x = queue.popleft()
print(x)  # Output: 1
print(queue)  # Output: deque([2, 3])

# Peeking the first element of the queue - O(1)
first = queue[0]
print(first)  # Output: 2

# Checking if the queue is empty - O(1)
if queue:
    print("Queue is not empty")

# Iterating through the queue - O(n)
for element in queue:
    print(element)

# Removing all elements from the queue using clear method - O(n)
queue.clear()
print(queue)  # Output: deque([])
