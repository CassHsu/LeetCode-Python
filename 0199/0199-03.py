class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        rs = []
        
        def rsv(node, lvl):
            if lvl == len(rs):
                rs.append(node.val)
                
            for n in [node.right, node.left]:
                if n:
                    rsv(n, lvl + 1)
        
        rsv(root, 0)
        return rs
