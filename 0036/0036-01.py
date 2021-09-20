class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(nums: List) -> bool:
            nums = list(filter(lambda n: n != '.', nums))
            return len(set(nums)) == len(nums)
        
        SW = 9
        GW = 3
        
        for i in range(SW):
            if not check(board[i]):
                return False
            
            if not check([k[i] for k in board]):
                return False
            
        for i in range(0, SW, GW):
            for j in range(0, SW, GW):
                if not check([board[i + m][j + k] for m in range(GW) for k in range(GW)]):
                    return False
        
        return True
