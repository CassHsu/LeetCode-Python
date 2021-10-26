class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
		
        prev, count = intervals[0][1], 1
        
        for index in range(1, len(intervals)):
            if intervals[index][0] >= prev:
                count += 1
                prev = intervals[index][1]
        
        return len(intervals) - count
