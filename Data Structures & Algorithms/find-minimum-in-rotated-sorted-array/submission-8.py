class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums [mid]:
                return nums[mid]
            elif nums[mid] > nums[r]:
               l = mid + 1
            else:
                r = mid

        # l = 0
        # r = len(nums) - 1
        
        # if len(nums) == 1:
        #     return nums[0]

        # while l < r:
        #     mid = (l + r) // 2
        #     if nums[mid] > nums[mid+1]:
        #         return nums[mid + 1]
        #     elif nums[mid - 1] > nums[mid]:
        #         return nums[mid]
        #     elif nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid
                        