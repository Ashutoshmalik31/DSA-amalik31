class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        min_best = nums[0]
        max_best = nums[0]
        num1, num2 = nums[0], nums[0]
        for i in range(1, len(nums)):
            num1 = max(nums[i], nums[i] + num1)
            num2 = min(nums[i], nums[i] + num2)
            max_best = max(max_best, num1)
            min_best = min(min_best, num2) 
        if max_best < 0:
            return max_best
        return max(max_best, nums_sum - min_best)
        