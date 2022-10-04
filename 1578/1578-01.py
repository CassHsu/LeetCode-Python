class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        mx = 0
        
        for i, c in enumerate(colors):
            if i > 0 and c != colors[i - 1]:
                mx = 0
                
            total += min(mx, neededTime[i])
            mx = max(mx, neededTime[i])
            
        return total
