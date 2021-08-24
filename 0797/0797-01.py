class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        size = len(graph)
        
        def backtrack(path, curr):
            if curr + 1 == size:
                ans.append(list(path))
								return
            
            for i in graph[curr]:
                path.append(i)
                backtrack(path, i)
                path.pop()
        
        backtrack([0], 0)
        return ans
