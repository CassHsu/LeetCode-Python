class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count = 0
        def dfs(node):
            nonlocal count
            
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            count = max(count, l + r)
            return max(l, r) + 1
            
        dfs(root)
        return count
