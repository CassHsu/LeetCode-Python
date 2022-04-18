class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        res = self.dfs(root, res)
        
        tree = TreeNode()
        tree.val = 0
        curr = tree
        
        for v in res:
            t = TreeNode()
            t.val = v
            tree.right = t
            tree = tree.right
            
        return curr.right      
    
    
    def dfs(self, node: TreeNode, res) -> list:
        if not node:
            return None
        
        if node.left:
            res = self.dfs(node.left, res)
            
        res.append(node.val)
        
        if node.right:
            res = self.dfs(node.right, res)
            
        return res
