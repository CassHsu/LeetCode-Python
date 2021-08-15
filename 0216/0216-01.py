class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def backtrack(curr, start, remain):
            nonlocal k, n
            if len(curr) == k:
                if remain == 0:
                    ans.append(list(curr))
                    return
                return
            
            for i in range(start, 10):                       
                curr.append(i)
                backtrack(curr, i + 1, remain - i)
                curr.pop()
            
        
        backtrack([], 1, n)
        return ans
