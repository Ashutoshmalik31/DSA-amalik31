class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        start = 0
        end = len(nums) - 1
        peak_element = self.findPeak(nums)
        print(peak_element)
        left = self.targeted_search(nums, start, peak_element, target)
        right = self.targeted_search(nums, peak_element + 1, end, target)
        if left != -1:
            return left
        elif right != -1:
            return right

        return -1


    def findPeak(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums [mid]:
                return mid - 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

    def targeted_search(self, nums, start, end, target):
        while start <= end:
            mid = (start + end)// 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid    
        return -1






    # def targeted_search(self, nums, start, end, target):
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if nums[mid] > target:
    #             end = mid - 1
    #         elif nums[mid] < target:
    #             start = mid + 1
    #         else:
    #             return mid
    #     return -1

    # def peak_element(self, nums):
    #     l = 0
    #     r = len(nums) - 1
    #     while l < r:
    #         mid = l + (r - l) // 2
    #         if nums[mid] > nums[mid + 1]:
    #             return mid
    #         elif nums[mid] > nums[r]:
    #             l = mid + 1
    #         elif nums[mid - 1] > nums[mid]:
    #             return mid - 1
    #         else:
    #             r = mid