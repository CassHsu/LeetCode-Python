class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(postorder.pop())
        if len(preorder) == 1:
            return root
        
        i = preorder.index(postorder[-1])
        
        root.right = self.constructFromPrePost(preorder[i:],  postorder)
        root.left  = self.constructFromPrePost(preorder[1:i], postorder)
        return root
