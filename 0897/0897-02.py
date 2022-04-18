class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:        
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inorder(node.right)
        
        self.curr = TreeNode(None)
        ans = self.curr
        inorder(root)
        return ans.right
