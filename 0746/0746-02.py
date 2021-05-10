class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def mincost(i):
            if i <= 1:
                return 0
            
            if i in cache:
                return cache[i]
            
            step1 = cost[i-1] + mincost(i-1)
            step2 = cost[i-2] + mincost(i-2)
            cache[i] = min(step1, step2)
            return cache[i]
        
        cache = {}
        return mincost(len(cost))
