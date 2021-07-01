class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        
        def preorder(r):
            if r == None:
                return
            
            ret.append(r.val)
            preorder(r.left)    
            preorder(r.right)
            
        preorder(root)
        return ret;
