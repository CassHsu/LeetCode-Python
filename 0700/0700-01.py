class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
