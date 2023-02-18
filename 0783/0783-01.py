class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        min_diff = float('inf')

        def dfs(node: TreeNode):
            if node == None:
                return

            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)

        for i in range(1, len(values)):
            min_diff = min(min_diff, abs(values[i] - values[i - 1]))
            
        return min_diff
