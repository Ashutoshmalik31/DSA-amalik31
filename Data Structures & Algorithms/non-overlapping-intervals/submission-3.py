class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        res = 0
        previous = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= previous:
                previous = end
            else:
                res += 1
                previous = min(end, previous)
        return res
        