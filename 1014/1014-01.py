class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prev = ans = -float('inf')
        
        for i in range(1, len(values)):
            prev = max(prev, values[i-1] + i - 1)
            ans = max(ans, prev + values[i] - i)
            
        return ans
