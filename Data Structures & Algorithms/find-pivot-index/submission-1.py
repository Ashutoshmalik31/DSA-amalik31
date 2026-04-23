class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = self.prefixSum(nums)
        n = len(nums) - 1
        for idx in range(len(nums)):
            first_half = prefix[idx - 1] if idx > 0 else 0
            second_half = prefix[n] - prefix[idx]
            if first_half == second_half:
                return idx
        return -1

    def prefixSum(self, nums):
        numsSum = []
        curSum = 0
        for num in nums:
            curSum += num
            numsSum.append(curSum)
        return numsSum

