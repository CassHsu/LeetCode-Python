class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        m = { node: Node(node.val) }
        self.dfs(node, m)
        return m[node]
    
    def dfs(self, node, m):
        for n in node.neighbors:
            if n not in m:
                m[n] = Node(n.val)
                self.dfs(n, m)
                
            m[node].neighbors.append(m[n])
