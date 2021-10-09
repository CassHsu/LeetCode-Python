class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        
        def backtrack(curr, idx):
            if len(curr) == len(s):
                tmp = "".join(curr)
                if not tmp in ans:
                    ans.append(tmp)
                return
            
            for i in range(idx, len(s)):
                curr.append(s[i].lower())
                backtrack(curr, i+1)
                curr.pop()
                
                curr.append(s[i].upper())
                backtrack(curr, i+1)
                curr.pop()
        
        backtrack([], 0)
        return ans
