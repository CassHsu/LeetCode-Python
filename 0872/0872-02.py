class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return str(node.val)
            
            ret = []
            if node.left:
                ret.append(dfs(node.left))
                
            if node.right:
                ret.append(dfs(node.right))
                
            return "-".join(ret)
        
        return dfs(root1) == dfs(root2)
