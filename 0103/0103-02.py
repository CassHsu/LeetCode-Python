from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        q = deque([])
        q.append(deque((root, 0)))
        while q:
            t = q.popleft()
            node = t[0]
            lv = t[1]
            
            if len(ans) <= lv:
                ans.append(deque())
            
            if lv % 2 == 0:
                ans[lv].append(node.val)
            else:
                ans[lv].appendleft(node.val)
                    
            if node.left:
                q.append((node.left, lv + 1))
            if node.right:
                q.append((node.right, lv + 1))
            
        return ans
