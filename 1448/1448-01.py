class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node, mx):
            nonlocal count
            
            if mx <= node.val:
                count += 1
            
            if node.right:
                dfs(node.right, max(node.val, mx))
                
            if node.left:
                dfs(node.left, max(node.val, mx))
                
        dfs(root, float('-inf'))
        return count
