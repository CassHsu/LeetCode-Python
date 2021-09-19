class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(0, numRows):
            row = [1 for _ in range(i+1)]
            
            for j in range(1, i):
                row[j] = ans[-1][j] + ans[-1][j - 1]
                
                
            ans.append(row)
            
        return ans
