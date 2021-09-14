class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return False
        
            l = dfs(node.left)
            r = dfs(node.right)
            m = (node == p or node == q)
            
            check = [1 if v else 0 for v in [l, r, m]]
            if sum(check) >= 2:
                ans = node
                
            return m or l or r
            
        
        dfs(root)
        return ans
