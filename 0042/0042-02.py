class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        l = 0
        r = n - 1
        ans = 0
        
        ml = height[0]
        mr = height[-1]
        
        while l <= r:
            ml = max(ml, height[l])
            mr = max(mr, height[r])
            
            if ml < mr:
                ans += ml - height[l]
                l += 1
            else:
                ans += mr - height[r]
                r -= 1
        
        return ans
