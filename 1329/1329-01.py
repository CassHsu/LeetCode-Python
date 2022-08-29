class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        diagonals = defaultdict(list)
        
        for r in range(m):
            for c in range(n):
                diagonals[r - c].append(mat[r][c])
                
        for d in diagonals.values():
            heapq.heapify(d)
            
        for r in range(m):
            for c in range(n):
                v = heapq.heappop(diagonals[r - c])
                mat[r][c] = v
        
        return mat
