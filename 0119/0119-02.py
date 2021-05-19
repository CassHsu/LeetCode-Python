class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        arr = self.getRow(rowIndex-1)
        return [sum(x) for x in zip ([0] + arr, arr + [0])]
