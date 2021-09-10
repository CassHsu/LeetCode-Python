class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        q = collections.deque([(root, 1)])
        
        while q:
            n, d = q.popleft()
            
            if n:
                if not n.left and not n.right:
                    return d
                else:
                    q.append((n.left, d + 1))
                    q.append((n.right, d + 1))
