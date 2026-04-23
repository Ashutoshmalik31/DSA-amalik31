class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        res = []
        for num in range(len(nums)):
            if num + k <= len(nums):
                res.append(max(nums[num:num + k]))
        return res

        