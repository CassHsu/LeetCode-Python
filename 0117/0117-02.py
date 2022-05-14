class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = collections.deque([root])
        while q:
            size = len(q)
            
            for i in range(size):
                n = q.popleft()
                
                if i < size - 1:
                    n.next = q[0]
                    
                if n.left:
                    q.append(n.left)
                    
                if n.right:
                    q.append(n.right)
                    
        return root
