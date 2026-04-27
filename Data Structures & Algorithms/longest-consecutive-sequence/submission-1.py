class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        final_len = 0
        seen = set()
        for i in range(len(nums)):
            length = 1
            if nums[i] - 1 not in seen:
                res = nums[i] + 1
                while res in nums:
                    length += 1
                    res += 1
                final_len = max(final_len, length)
            seen.add(nums[i])
        return final_len

        
        
        
        
        
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # seen = set(nums)
        # longest = 0
        # for num in nums:
        #     length = 0
        #     if num - 1 not in seen:
        #         length = 1
        #         res = num
        #         while res + 1 in seen:
        #             res += 1
        #             length += 1
        #         longest = max(longest, length)
        # return longest