class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        
        def dfs(n, lv):
            if n is None:
                return
            
            if lv == depth - 1:
                n.left = TreeNode(val, left=n.left)
                n.right = TreeNode(val, right=n.right)
                return
            
            dfs(n.left, lv + 1)
            dfs(n.right, lv + 1)
            
        dfs(root, 1)
        return root
