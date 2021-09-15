class Solution:
    def connect(self, root: 'Node') -> 'Node':
        m = {}
        
        def dfs(root, lv):
            if not root:
                return None
            
            root.next = m[lv] if lv in m else None
            m[lv] = root
            dfs(root.right, lv + 1)
            dfs(root.left,  lv + 1)
            
        dfs(root, 0)
        return root
