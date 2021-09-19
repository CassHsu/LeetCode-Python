from collections import deque

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(mat) * len(mat[0])
        if r * c != size:
            return mat
        
        ans = []
        q = deque([])
        for row in mat:
            for v in row:
                q.append(v)
                
        for _ in range(r):
            row = []
            for _ in range(c):
                row.append(q.popleft())
                
            ans.append(row)
        
        return ans
