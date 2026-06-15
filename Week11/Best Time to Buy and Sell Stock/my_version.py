def maxProfit(prices):
    i = 0
    j = 1
    profit = 0

    while j < len(prices):
        profit = max(profit, max(prices[j:]) - prices[i])

        i += 1
        j += 1 

    if profit:
        return profit
    else:
        return 0

# Time Complexity - O(n^2) 
# This is due to finding the maximum value in the subarray prices[j:] for each iteration of 
# the while loop, which takes O(n) time. Since the while loop runs n times, the overall 
# time complexity is O(n^2).
