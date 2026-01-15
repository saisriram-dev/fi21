# 3D-Lists in python

# A simple example
cube = [
    [  # Layer 0
        [1, 2, 3],
        [4, 5, 6]
    ],
    [  # Layer 1
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print(cube)
# Output: [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
print(cube[0][1][2]) # Prints 6
print(cube[1][0][0]) # Prints 7

# Looping through the 3D List
for layer in cube:
    for row in layer:
        for value in row:
            print(value, end=" ")
    print()
