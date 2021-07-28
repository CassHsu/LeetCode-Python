class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return str(node.val)
            
            ret = ""
            if node.left:
                v = dfs(node.left)
                ret = v if ret == "" else ret + "-" + v
            if node.right:
                v = dfs(node.right)
                ret = v if ret == "" else ret + "-" + v
                
            return ret
        
        return dfs(root1) == dfs(root2)
