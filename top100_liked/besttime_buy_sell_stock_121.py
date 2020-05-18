
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy, profit = float('inf'), 0
        for p in prices:
            buy, profit = min(p, buy), max(profit, p- buy)

        print("buy :", buy)
        print("profit :", profit)

        return profit

# below is another approach which is not best optimised (time limit exceeded)

#         is_sorted = all(x>=y for x, y in zip(prices[:-1], prices[1:]))
#         if is_sorted: return 0

#         max_ = 0

#         for i in range(0, len(prices)-1):
#             for j in range(i, len(prices)):
#                 if prices[j] > prices[i]:
#                     current = prices[j]-prices[i]
#                     if current > max_: max_ = current

#         return max_
