class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ''
            
            res = ''
            res += str(node.val)
            
            if not node.left and not node.right:
                return res
            
            res += '('
            res += dfs(node.left)
            res += ')'
                
            l = dfs(node.right)
            if l:
                res += '('
                res += l
                res += ')'
            
            return res
            
        return dfs(root)
