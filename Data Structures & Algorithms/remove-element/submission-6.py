class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = 0
        # j = len(nums) - 1
        # while i <= j:
        #     if nums[j] == val:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #     else:
        #         i += 1
        # return i    

        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1  # Move j left since we put val at position j
            else:
                i += 1  # Keep non-val element, move i right
        return i   