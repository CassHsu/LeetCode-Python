class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            
            l = check(node.left)
            r = check(node.right)
            
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            
            return max(l, r) + 1
        
        return check(root) != -1
