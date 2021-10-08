class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        ldp = [0] * n
        rdp = [0] * n
        
        ldp[0] = height[0]
        rdp[-1] = height[-1]
        
        for i in range(1, n):
            ldp[i] = max(ldp[i-1], height[i])
            
        for i in range(n-2, -1, -1):
            rdp[i] = max(rdp[i+1], height[i])
            
        ans = 0
        for i in range(n):
            ans += min(ldp[i], rdp[i]) - height[i]
        
        return ans
