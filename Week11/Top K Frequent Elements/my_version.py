def topk(nums, k):
    def count(arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return list(freq.keys())

    frequency = count(nums)
    return frequency[:k]


"""
for num in arr:
    freq[num] = freq.get(num, 0) + 1 ------> O(n)

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) -----> O(m log m)
where m is the number of unique elements in the array.

return list(freq.keys()) -----> O(m) (There are m unique keys in the frequency dictionary)

return frequency[:k] -----> O(k) (Slicing the list to get the top k elements)

Overall Time complexity:
    O(n + m log m + m + k) = O(n + m log m)
    n == m in this question, so the overall time complexity is O(n log n)

"""
