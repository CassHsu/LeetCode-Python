class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        size = len(intervals)
        m = {}
        
        for i in range(size):
            for j in range(size):
                if i != j:
                    if intervals[i][0] <= intervals[j][0]:
                        if intervals[i][1] >= intervals[j][1]:
                            inter = (intervals[j][0], intervals[j][1])
                            if inter not in m:
                                m[inter] = True
                                count += 1
                                continue     
        return size - count
