class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        l, r = root.left, root.right
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        root.left, root.right = None, l
        
        while root.right:
            root = root.right
            
        root.right = r
