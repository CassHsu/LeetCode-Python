class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = 0
        
        prev = 0
        for _, end in intervals:
            if end > prev:
                count += 1
                prev = end
                
        return count
