class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(s, left, right):
            if len(s) == n*2:
                res.append(s)
                return
            
            if left > right:
                backtrack(s + ")", left, right + 1)
                
            if left < n:
                backtrack(s + "(", left + 1, right)
            return
        
        backtrack("", 0, 0)
        return res
