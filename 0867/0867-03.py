class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for c in range(len(matrix[0])):
            t = []
            for r in range(len(matrix)):
                t.append(matrix[r][c])
                
            ans.append(t)
        
        return ans
