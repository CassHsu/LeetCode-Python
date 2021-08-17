class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def backtrack(curr, start):
            if start >= len(s):
                ans.append(list(curr))
                return
            
            for i in range(start, len(s)):
                c = s[start: i + 1]
                # print(start, i, c)
                
                if c == c[::-1]:
                    curr.append(c)
                    backtrack(curr, i + 1)
                    curr.pop()
        
        
        backtrack([], 0)
        return ans
