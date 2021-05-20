class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        last = self.getRow(rowIndex - 1)
        row = [1]
        for j in range(0, len(last) - 1):
            row.append(last[j] + last[j+1])
            
        row.append(1)
        return row
