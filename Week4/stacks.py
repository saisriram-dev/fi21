# Stacks
# LIFO means Last In First Out
# We can use a list to implement a stack in Python
# Top element of the stack is the last element of the list
stack = []

# Adding elements to the stack - O(1)
stack.append(1)
stack.append(2)
stack.append(3)

# Removing(pop) the top element from the stack - O(1)
# We can't pop from an empty stack, so we should check if the stack is not empty before popping'
x = stack.pop()
print(x)  # Output: 1
print(stack)  # Output: [1, 2]

# Peeking the top element of the stack - O(1)
top = stack[-1]
print(top)  # Output: 2

# Checking if the stack is empty - O(1)
if stack:
    print("Stack is not empty")
