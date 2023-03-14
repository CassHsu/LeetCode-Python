from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        dq = deque([(root.left, root.right)])
        while dq:
            l, r = dq.popleft()

            if not l and not r:
                continue

            if l and r and l.val == r.val:
                dq.append((l.left, r.right))
                dq.append((l.right, r.left))
            else:
                return False

        return True
