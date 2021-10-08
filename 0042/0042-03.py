class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        i = 0
        
        while i < len(height):
            if (not stack or height[i] < height[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                tmp = stack.pop()
                
                if not stack:
                    continue
                    
                h = min(height[i], height[stack[-1]]) - height[tmp]
                ans += (h * (i - stack[-1] - 1))
                
        return ans
