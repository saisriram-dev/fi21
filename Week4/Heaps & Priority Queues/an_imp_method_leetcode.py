# Putting tuples of items on heaps
from collections import Counter
import heapq

# The Counter function would give us a dictionary of the keys = items and values = counts
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
counter = Counter(D)  # Output: Counter({5: 4, 4: 3, 3: 2})

heap = []
for k, v in counter.items():
    heapq.heappush(
        heap, (v, k)
    )  # We push the count first so that the heap is ordered by count

print(heap)
""" Output: [(2, 3), (3, 4), (4, 5)] first element of the tuple is the count and 
            the second element is the item """
