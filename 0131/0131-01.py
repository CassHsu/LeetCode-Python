class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def is_palindrome(p):
            # print(p)
            if p == p[::-1]:
                return True
            return False
                
        
        def backtrack(curr, start):
            if start >= len(s):
                ans.append(list(curr))
                return
            
            for i in range(start, len(s)):
                tmp = s[start: i + 1]
                if is_palindrome(tmp):
                    curr.append(tmp)
                    backtrack(curr, i + 1)
                    curr.pop()
            
        backtrack([], 0)
        return ans
