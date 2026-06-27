from collections import Counter


def topk(nums, k):
    counter = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in counter.items():
        buckets[freq].append(num)

    res = []

    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)

            if len(res) == k:
                return res


"""
We eliminated the sorting step by using a bucket sort approach. 
Instead of sorting the frequency dictionary, we create buckets where the index represents the 
frequency of the elements.

That is first buckets -> elements with frequency 0,
second buckets -> elements with frequency 1, and so on. 
So indirectly we eliminate the sorting step by placing elements in their respective buckets 
based on their frequency.

Then we iterate through the buckets in reverse order (starting from the highest frequency) 
and collect the elements until we have collected k elements. 

Time complexity:
    O(n) to count the frequency of each element using Counter.
    O(n) to create the buckets and place elements in their respective buckets based on their frequency.
    O(n) in the worst case to iterate through the buckets and collect the top k elements (if all elements are unique).

Overall time complexity: O(3n) = O(n)
"""
