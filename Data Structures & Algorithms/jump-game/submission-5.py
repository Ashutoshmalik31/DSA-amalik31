class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            test = i + nums[i]
            if nums[i] > 0 and test >= reach:
                reach = i
        return reach == 0