class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        lvls = []
        
        def traversal(node, lv):
            if not node:
                return
            
            if len(lvls) <= lv:
                lvls.append([node.val])
            else:
                lvls[lv].append(node.val)
                
            traversal(node.left, lv+1)
            traversal(node.right, lv+1)
            return
        
        traversal(root, 0)
        for lvl in lvls:
            ans.append(lvl[-1])
        
        return ans
