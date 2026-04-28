class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        area = 0
        largest_area = 0
        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            largest_area = max(largest_area, area)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return largest_area
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # i, j = 0, len(heights) - 1
        # large_area = 0
        # while i < j:
        #     area = min(heights[i], heights[j]) * (j - i)
        #     large_area = max(area, large_area)
        #     if heights[i] < heights[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return large_area           