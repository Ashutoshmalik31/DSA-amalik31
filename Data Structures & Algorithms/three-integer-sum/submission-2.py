class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1   
        return result

        # res = []
        # nums.sort()
        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i - 1]:
        #         continue
        #     l = i + 1
        #     r = len(nums) - 1
        #     while l < r:
        #         threesum = nums[i] + nums[l] + nums[r]
        #         if threesum > 0:
        #             r -= 1
        #         elif threesum < 0:
        #             l += 1
        #         else:
        #             res.append([nums[i], nums[l], nums[r]])
        #             l += 1
        #             while l < r and nums[l] == nums[l-1]:
        #                 l = l+1
        # return res 