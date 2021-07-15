class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        
        for i, t in enumerate(timeSeries):
            count += duration
            if i > 0:
                diff = t - timeSeries[i - 1]
                if diff < duration:
                    count -= (duration - diff)
                
        return count
