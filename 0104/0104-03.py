class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left) + 1
            r = dfs(node.right) + 1
            return max(l, r)
            
        count = max(dfs(root), count)
        return count
