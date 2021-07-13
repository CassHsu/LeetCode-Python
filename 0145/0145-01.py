class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        
        def postorder(node):
            if node == None:
                return
            
            postorder(node.left)
            postorder(node.right)
            ret.append(node.val)
            
        postorder(root)
        return ret
