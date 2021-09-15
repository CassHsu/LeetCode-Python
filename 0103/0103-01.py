from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        ans = []
        
        def bfs(node, lv):
            if not node:
                return
            
            if len(ans) <= lv:
                ans.append(deque([node.val]))
            else:
                if lv % 2 == 0:
                    ans[lv].append(node.val)
                else:
                    ans[lv].appendleft(node.val)
                
            bfs(node.left,  lv + 1)
            bfs(node.right, lv + 1)
            return
    
        bfs(root, 0)
        return ans
