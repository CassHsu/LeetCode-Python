class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        if not s:
            return 0
        if is_palindrome(s):
            return 1
        return 2
