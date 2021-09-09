class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def preorder(node):
            if not node:
                return
            
            ans.append(node.val)
            
            preorder(node.left)
            preorder(node.right)
            return
            
        preorder(root)
        return ans
