class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def sol(n):
            if not n:
                return 0, 0, float('inf')
            
            l = sol(n.left)
            r = sol(n.right)
            
            dp0 = l[1] + r[1]
            dp1 = min(l[2] + min(r[1:]), r[2] + min(l[1:]))
            dp2 = 1 + min(l) + min(r)
            
            return dp0, dp1, dp2
        
        return min(sol(root)[1:])
