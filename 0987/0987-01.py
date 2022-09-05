class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        cols = defaultdict(list)
        mi = 0
        mx = 0
        
        def dfs(n, r, c):
            if n is not None:
                nonlocal mi, mx, cols
                cols[c].append((r, n.val))
                mi = min(mi, c)
                mx = max(mx, c)
                
                dfs(n.left, r + 1, c - 1)
                dfs(n.right, r + 1, c + 1)
        
        dfs(root, 0, 0)
        
        res = []
        for c in range(mi, mx + 1):
            res.append([v for r, v in sorted(cols[c])])
            
        return res
