class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        previous = intervals[0][1]
        output = 0
        for start, end in intervals[1:]:
            if start < previous:
                output += 1
                previous = min(end, previous)
            else:
                previous = end    
        return output
                








        