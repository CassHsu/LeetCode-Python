class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def init():
            return [[''] * 3 for _ in range(3)]
        
            
        def is_draw(rows):
            for row in rows:
                for r in row:
                    if r == '':
                        return False
            return True
        
        
        def is_win(rows, t):
            if rows[0][0] == t and rows[1][1] == t and rows[2][2] == t:
                return True
            
            if rows[0][2] == t and rows[1][1] == t and rows[2][0] == t:
                return True
            
            for i in range(3):
                if rows[i][0] == t and rows[i][1] == t and rows[i][2] == t:
                    return True
                if rows[0][i] == t and rows[1][i] == t and rows[2][i] == t:
                    return True
                
            return False
            
        
        if len(moves) < 5:
            return "Pending"
        
        board = init()
        turn = 'A'
        for i, move in enumerate(moves):
            board[move[0]][move[1]] = turn
            
            if is_win(board, turn):
                return turn
            
            turn = 'B' if turn == 'A' else 'A'
        
        if is_draw(board):
            return "Draw"
        return "Pending"
