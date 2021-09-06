from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(m, n):
            if not m and not n:
                return True
            if not m or not n:
                return False
            return m.val == n.val
        
        dq = deque([(p, q)])
        while dq:
            m, n = dq.popleft()
            if not check(m, n):
                return False
            
            if m:
                dq.append((m.left, n.left))
                dq.append((m.right, n.right))
        
        return True
