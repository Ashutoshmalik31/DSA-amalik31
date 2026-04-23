class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = self.value_indexing(nums)
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in present:
                if i != present[diff]:
                    return[i, present[diff]]
        return [-1, -1]

    def value_indexing(self, nums):
        index_dict = {}
        index = 0
        for num in nums:
            index_dict[num] = index 
            index += 1
        return index_dict              