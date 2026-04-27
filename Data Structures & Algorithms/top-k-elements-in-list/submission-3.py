class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        freq = sorted(seen.items(), key= lambda x: x[1], reverse = True)
        result = []
        for i,j in freq:
            result.append(i)
            k -= 1
            if k == 0:
                break
        return result
            


































        # seen = defaultdict(int)
        # for num in nums:
        #     if num not in seen:
        #         seen[num] = 1
        #     else:
        #         seen[num] += 1

        # freq_sorted = sorted(seen.items(), key=lambda x: x[1], reverse= True)
        # res = []
        # for key, value in freq_sorted:
        #     res.append(key)
        #     k -= 1
        #     if k == 0:
        #         break
        # return res           