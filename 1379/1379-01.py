class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(origin, clone):
            if origin:
                inorder(origin.left, clone.left)
                
                if origin is target:
                    self.ans = clone
                    
                inorder(origin.right, clone.right)
                
        inorder(original, cloned)
        return self.ans
