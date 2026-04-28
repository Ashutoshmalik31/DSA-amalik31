class Solution:
    def maxProfit(self, price: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while  r < len(price):
            if price[l] >= price[r]:
                l = r
                r += 1
            else:
                profit = max(profit, price[r] - price[l])
                r += 1
        return profit
        # l, r = 0, 1
        # profit = 0
        # while r < len(price):
        #     if price[r] > price[l]:
        #        profit = max(profit, price[r] - price[l])
        #        r += 1
        #     else:
        #         l = r
        #         r += 1
        # return profit        