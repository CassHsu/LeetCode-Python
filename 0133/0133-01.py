class Solution:
    def __init__(self):
        self.m = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.m:
            return self.m[node]
        
        clone = Node(node.val, [])
        self.m[node] = clone
        
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return self.m[node]
