class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mid = 0
        m = {}
        
        def array_to_tree(l, r):
            if l > r:
                return None
            
            nonlocal mid
            root_val = preorder[mid]
            root = TreeNode(root_val)
            
            mid += 1
            root.left  = array_to_tree(l, m[root_val] - 1)
            root.right = array_to_tree(m[root_val] + 1, r)
            return root
            
            
        for i, v in enumerate(inorder):
            m[v] = i
            
        return array_to_tree(0, len(preorder) - 1)
