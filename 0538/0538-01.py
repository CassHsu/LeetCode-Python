class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return root
        
    def dfs(self, root: TreeNode, total: int) -> int:
        if not root:
            return total
        
        root.val += self.dfs(root.right, total)
        return self.dfs(root.left, root.val)
