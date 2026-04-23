class Solution:
    def maxProfit(self, price: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(price):
            if price[r] > price[l]:
               profit = max(profit, price[r] - price[l])
               r += 1
            else:
                l = r
                r += 1
        return profit        