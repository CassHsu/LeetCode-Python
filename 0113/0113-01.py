class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        
        ret = []
        
        def backtrack(node, l):
            if not any([node.left, node.right]):
                if sum(l) == targetSum:
                    ret.append(l)
                return
            
            if node.left: 
                backtrack(node.left, l+[node.left.val])
                
            if node.right: 
                backtrack(node.right, l+[node.right.val])
            
        backtrack(root, [root.val])
        return ret
