# Building max heaps
import heapq

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
A = [-x for x in A]  # Negate the values to use min heap as max heap
heapq.heapify(A)

""" As we negated the values, the smallest value which is originally -4 will become 4 and 
    the largest value which is originally 12 will become -12. So we could use the min heap to 
    implement the max heap by negating the values. And the first element of the heap will be the 
    largest value in the original list (before negation).
"""
largest = -heapq.heappop(A)
print(largest)  # Output: 12, which is the largest value in the original list

# To get the top k largest elements from the list
k = 3
top_k_largest = [-heapq.heappop(A) for _ in range(k)]
print(top_k_largest)  # Output: [10, 9, 8], which are the top 3 largest values in the original list

# If we were to push an element in the max heap, say 7 we need to negate it before pushing
heapq.heappush(A, -7)
print(A)  # The heap will maintain the max heap property based on the negated values
