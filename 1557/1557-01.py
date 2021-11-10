class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        S = set(range(n))
        
        for x, y in edges:
            if y in S:
                S.remove(y)
                
        return list(S)
