class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonely = []
        
        def dfs(node):
            if node == None:
                return
            
            if node.right and not node.left:
                lonely.append(node.right.val)
            if not node.right and node.left:
                lonely.append(node.left.val)
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return lonely
