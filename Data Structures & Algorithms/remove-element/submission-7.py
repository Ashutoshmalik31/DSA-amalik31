class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] != val:
                i += 1
            elif nums[j] == val:
                j -= 1
            else:
                nums [i], nums[j] = nums[j], nums[i]
        return i      