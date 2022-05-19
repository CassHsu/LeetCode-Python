class Solution:
    rank = {}
    graph = defaultdict(list)
    conn_dict = {}
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.formGraph(n, connections)
        self.dfs(0, 0)
        
        result = []
        for u, v in self.conn_dict:
            result.append([u, v])
        
        return result
            
    def dfs(self, node: int, discovery_rank: int) -> int:
        if self.rank[node]:
            return self.rank[node]

        self.rank[node] = discovery_rank
        
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue
                  
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)
            
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]
            
            min_rank = min(min_rank, recursive_rank)
        
        return min_rank
    
    def formGraph(self, n: int, connections: List[List[int]]):
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}
        
        for i in range(n):
            self.rank[i] = None
        
        for edge in connections:
            
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)
            
            self.conn_dict[(min(u, v), max(u, v))] = 1
