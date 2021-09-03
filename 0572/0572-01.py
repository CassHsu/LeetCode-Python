class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        def is_same(n1, n2):
            if not n1 and not n2:
                return True
            
            elif n1 and n2:
                return n1.val == n2.val and is_same(n1.left, n2.left) and is_same(n1.right, n2.right)
            
            else:
                return False
        
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
