class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost) + 1
        min_cost = [0] * size
        
        for i in range(2, size):
            step1 = min_cost[i-1] + cost[i-1]
            step2 = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(step1, step2)
            
        return min_cost[-1]
