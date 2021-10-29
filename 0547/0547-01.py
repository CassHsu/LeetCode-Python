class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(node):
            nonlocal n
            visited[node] = True
            
            for i in range(n):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)
                    
        ret = 0
        for i in range(n):
            if not visited[i]:
                ret += 1
                dfs(i)
                
        return ret
