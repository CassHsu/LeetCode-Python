class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def contains_1(node):
            if not node:
                return False
            
            is_left_1 = contains_1(node.left)
            is_right_1 = contains_1(node.right)
            
            if not is_left_1:
                node.left = None
                
            if not is_right_1:
                node.right = None
                
            return node.val or is_left_1 or is_right_1
        
        return root if contains_1(root) else None
