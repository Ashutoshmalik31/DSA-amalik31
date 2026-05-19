class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))

        return res


        # maxarea = 0
        # stack = []
        # for i,h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         index, height = stack.pop()
        #         maxarea = max(maxarea, height * (i - index))
        #         start = index
        #     stack.append((start,h))

        # for i,h in stack:
        #     maxarea = max(maxarea, h * (len(heights) - i))

        # return maxarea

        