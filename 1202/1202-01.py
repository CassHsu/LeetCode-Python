class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = {}
        
        for node in range(len(s)):
            graph[node] = []
            
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
            
        position = {}
        for node in range(len(s)):
            if node not in position:
                idx = set()
                self.dfs(node, idx, graph)
                self.build(s, idx, position)
                
        res = ''
        for node in range(len(s)):
            res += position[node]
            
        return res
    
    def build(self, s, idx, position):
        idxs = list(idx)
        chars = []
        
        for i in idxs:
            chars.append(s[i])
            
        idxs.sort()
        chars.sort()
        
        for i in range(len(idxs)):
            position[idxs[i]] = chars[i]
            
    def dfs(self, node, idx, graph):
        idx.add(node)
        for n in graph[node]:
            if n not in idx:
                self.dfs(n, idx, graph)
