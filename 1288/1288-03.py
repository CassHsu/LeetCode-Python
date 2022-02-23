class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        count = 0
        
        for i in range(size):
            for j in range(size):
                if i != j and intervals[j][0] > 0 and intervals[j][1] > 0:
                    if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                            intervals[j] = (-1, -1)
                            count += 1
                            
        return size - count
