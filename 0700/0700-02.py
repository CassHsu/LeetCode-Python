class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root != None:
            if root.val == val:
                return root
            
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return None
