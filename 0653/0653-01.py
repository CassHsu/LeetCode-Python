class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root.left and not root.right:
            return False
        
        m = {}
        
        def traverse(node):            
            if not node:
                return
            
            m[node.val] = True
            traverse(node.left)
            traverse(node.right)
            return
        
        traverse(root)
        
        for n in m:
            if k - n != n and k - n in m:
                return True
        
        return False
