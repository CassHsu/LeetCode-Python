class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        
        if root:
            stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
                
            ans.append(node.val)
        
        return ans[::-1]
