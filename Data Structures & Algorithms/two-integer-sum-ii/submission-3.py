class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        result = []
        while start < end:
            if numbers[start] + numbers[end] == target:
                return[start+1, end+1]
            elif numbers[start] + numbers[end] > target:
                end = end - 1
            else:
                start = start + 1    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # start = 0
        # end = len(numbers) - 1
        # res = []
        # while start < end:
        #     if numbers[start] + numbers[end] < target:
        #         start += 1
        #     elif numbers[start] + numbers[end] > target:
        #         end -= 1
        #     elif numbers[start] + numbers[end] == target:
        #         res.append(start+1)
        #         res.append(end+1)
        #         return res
       