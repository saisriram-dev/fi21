def maxProfit(prices):
    i = 0  # Left pointer: Buy day
    j = 1  # Right pointer: Sell day
    profit = 0

    while j < len(prices):
        if prices[i] > prices[j]:
            # If today's price is cheaper than our buy day,
            # jump the buy day here immediately.
            i = j
        else:
            # If today's price is higher, check for max profit.
            profit = max(profit, prices[j] - prices[i])

        # The explorer ALWAYS moves forward every single turn
        j += 1

    return profit
