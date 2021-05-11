class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s1, s2 = 0, 0
        
        for i in range(2, len(cost) + 1):
            tmp = s1
            s1 = min(s1 + cost[i-1], s2 + cost[i-2])
            s2 = tmp
            
        return s1
