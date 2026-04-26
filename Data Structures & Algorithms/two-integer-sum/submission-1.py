class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        count = self.nums_counter(nums)
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in count:
                if i != count[diff]:
                    output.append(i)
                    output.append(count[diff])
                    break
        return [-1, -1] if output == [] else output

    def nums_counter(self, nums):
        res = {}
        index = 0
        for num in nums:
            res[num] = index
            index += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    #     present = self.value_indexing(nums)
    #     for i in range(len(nums)):
    #         diff = target - nums[i] 
    #         if diff in present:
    #             if i != present[diff]:
    #                 return[i, present[diff]]
    #     return [-1, -1]

    # def value_indexing(self, nums):
    #     index_dict = {}
    #     index = 0
    #     for num in nums:
    #         index_dict[num] = index 
    #         index += 1
    #     return index_dict              