class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        res = 0
        left_max = height[start]
        right_max = height[end]
        while start < end:
            if left_max <= right_max:
                start += 1
                left_max = max(left_max, height[start])
                res += left_max - height[start]
            else:
                end -= 1
                right_max = max(right_max, height[end])
                res += right_max - height[end]    
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l , r = 0, len(height) - 1
        # leftmax , rightmax = height[l], height[r]
        # res = 0
        # while l < r:
        #     if leftmax <= rightmax:
        #         l += 1
        #         leftmax = max(leftmax, height[l])
        #         res += leftmax - height[l]
        #     else:
        #         r -= 1
        #         rightmax = max(rightmax, height[r])
        #         res += rightmax - height[r]
        # return res