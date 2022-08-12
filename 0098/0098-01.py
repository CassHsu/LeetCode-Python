class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def vaild_BST(node, lower, upper):
            if not node:
                return True
            
            if lower and node.val <= lower.val:
                return False
            
            if upper and node.val >= upper.val:
                return False
            
            return vaild_BST(node.left, lower, node) and vaild_BST(node.right, node, upper)
        
        return vaild_BST(root, None, None)
