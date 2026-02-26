# Fixed length sliding window
""" This technique is used to solve problems that involve finding a subarray of a fixed length 
    that satisfies certain conditions. The idea is to maintain a window of a fixed size and slide it 
    across the array while keeping track of the necessary information to determine if the current 
    window satisfies the conditions."""

# To find the maximum average of a subarray of size k in an array of integers

def max_avg(arr, k):

    n = len(arr)
    curr_sum = 0

    for i in range(k):
        curr_sum += arr[i]
    
    max_avg = curr_sum / k

    for i in range(k, n):
        curr_sum += arr[i] # Add the new element
        curr_sum -= arr[i-k] # Remove the element that is sliding out of the window

        avg = curr_sum / k
        max_avg = max(max_avg, avg)

    return max_avg
