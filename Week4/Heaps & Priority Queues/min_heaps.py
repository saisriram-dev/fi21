# Build Min Heap
import heapq

# Defining the list
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

# Building the min heap
# Time complexity: O(n), Space complexity: O(1)
heapq.heapify(A)
print(A)

# Heap push (Insert an element into the heap)
# Time complexity: O(log n), Space complexity: O(1)
heapq.heappush(A, 4)
print(A)
# After heappush, the heap will be:
#             -4
#         /       \
#        0         1
#       / \       / \
#      3   2     5   10
#     / \       / \
#    8   9     12  4

# Heap peek (Return the smallest element without removing it)
# Time complexity: O(1), Space complexity: O(1)
print(A[0])  # Output: -4

# Heap pop (Remove and return the smallest element from the heap)
# Time complexity: O(log n), Space complexity: O(1)
min = heapq.heappop(A)
print(A, min)


# Heap sort (Sort the elements of the heap)
# Time complexity: O(n log n), Space complexity: O(n)
# Note: O(1) is possible via swapping, but it is complex to implement
def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [0] * len(arr)
    for i in range(len(arr)):
        sorted_arr[i] = heapq.heappop(arr)
    return sorted_arr


array = [5, 3, 8, 1, 2]
sorted_array = heap_sort(array)
print(sorted_array)

# Heap pushpop (Push an element and then pop the smallest element)
# Time complexity: O(log n), Space complexity: O(1)
result = heapq.heappushpop(A, 6)  # Push 6 and pop the smallest element (which is 0)
print(A, result)

# Building a heap from scratch
# Time complexity: O(nlog n)
C = [7, 2, 5, 3, 8]
heap = []
for item in C:
    heapq.heappush(heap, item)
    print(heap, len(heap))
