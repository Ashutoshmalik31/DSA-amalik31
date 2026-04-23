class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        res = []
        for num in range(len(nums)):
            if num + k <= len(nums):
                new_nums = nums[num:num + k]
                new_nums = sorted(new_nums)
                l = new_nums[-1]
                res.append(l)
        return res

        