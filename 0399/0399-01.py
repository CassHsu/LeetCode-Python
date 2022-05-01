class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(set)
        
        for i, (a, b) in enumerate(equations):
            cost = values[i]
            adj[a].add((b, cost))
            adj[b].add((a, 1 / cost))
            
        res = []
        for a, b in queries:
            if a not in adj or b not in adj:
                res.append(-1)
                continue
                
            stack = [(a, 1)]
            visited = set([a])
            
            while stack:
                a, cost = stack.pop()
                if a == b:
                    res.append(cost)
                    break
                    
                for _b, c in adj[a]:
                    if _b not in visited:
                        stack.append((_b, cost * c))
                        visited.add(_b)
            else:
                res.append(-1)
                
        return res
