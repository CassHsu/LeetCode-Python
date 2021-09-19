class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(mat) * len(mat[0])
        if r * c != size:
            return mat
        
        ans = []
        q = [v for row in mat for v in row]
        
        k = 0
        for _ in range(r):
            row = []
            for _ in range(c):
                row.append(q[k])
                k += 1
                
            ans.append(row)
        
        return ans
