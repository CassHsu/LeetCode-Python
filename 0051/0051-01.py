class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        state = [-1] * n
        r = 0
        
        print(state)
        
        def check(state, r):
            for i in range(r):
                if abs(state[r] - state[i]) == r - i or state[r] == state[i]:
                    return False
                
            return True
            
            
        def getPath(state):
            path = []
            for i in range(n):
                tmp_row = '.' * state[i] + 'Q' + '.' * (n - state[i] - 1)
                path.append(tmp_row)
            
            return path
            
        def dfs(state, r, res):
            if r == len(state):
                res.append(getPath(state))
            else:
                for i in range(n):
                    state[r] = i
                    if check(state, r):
                        r += 1
                        dfs(state, r ,res)
                        r -= 1
            
        dfs(state, r, res)
        return res
