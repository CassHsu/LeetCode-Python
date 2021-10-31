class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def recur(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] in ['X', 'Z']:
                return
            
            board[i][j] = 'Z'
            recur(i-1, j)
            recur(i+1, j)
            recur(i, j-1)
            recur(i, j+1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0, len(board)-1] or j in [0, len(board[0])-1]):
                    recur(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'O' if board[i][j] == 'Z' else 'X'
