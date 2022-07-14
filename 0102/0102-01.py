from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def traversal(node, lvl):
            if not node:
                return
            
            if len(ans) <= lvl:
                ans.append([node.val])
            else:
                ans[lvl].append(node.val)
                
            traversal(node.left, lvl + 1)
            traversal(node.right, lvl + 1)
            return
    
        traversal(root, 0)
        return ans
