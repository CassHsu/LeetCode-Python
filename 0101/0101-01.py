class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def invert(root):
            if not root:
                return None
            root.left, root.right = invert(root.right), invert(root.left)
            return root
        
        def same(m, n):
            if not m and not n:
                return True
            if not m or not n:
                return False
            if m.val != n.val:
                return False
            return same(m.left, n.left) and same(m.right, n.right)
        
        root.right = invert(root.right)
        return same(root.left, root.right)
