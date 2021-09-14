from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        dq = deque([root])
        
        while dq:
            count = len(dq)
            
            n = None
            for _ in range(count):
                n = dq.popleft()
                
                if n.left:
                    dq.append(n.left)
                if n.right:
                    dq.append(n.right)
            ans.append(n.val)
            
        return ans
