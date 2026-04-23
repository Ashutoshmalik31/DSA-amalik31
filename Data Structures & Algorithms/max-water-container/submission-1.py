class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        large_area = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            large_area = max(area, large_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return large_area           