class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        result = end
        while start <= end:
            k = start + (end - start)//2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/k)
            
            if hour > h:
                start = k + 1

            elif hour <= h:
                result = min(result, k)
                end = k - 1

        return result
      
        # start = 1
        # end = max(piles)
        # result = end
        # while start <= end:
        #     k = (start + end)//2
        #     hours = 0
        #     for pile in piles:
        #         hours += math.ceil(pile/k)
        #         print(hours)

        #     if hours <= h:
        #         result = min(result, k)
        #         end = k - 1
        #     else:
        #         start = k + 1   
        # return result
        