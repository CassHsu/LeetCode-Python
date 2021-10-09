class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(curr, m):
            nonlocal n, k
            if len(curr) == k:
                ans.append(list(curr))
                return
            
            for i in range(m, n+1):
                curr.append(i)
                backtrack(curr, i+1)
                curr.pop()
        
        backtrack([], 1)
        return ans
