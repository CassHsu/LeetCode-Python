class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, root, count):
        if root == None:
            return count
        
        count += 1
        l = self.dfs(root.left, count)
        r = self.dfs(root.right, count)
        
        return max(l, r)