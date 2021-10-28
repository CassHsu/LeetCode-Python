class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s).values()
        res = sum([n - (n % 2) for n in c])
        is_odd = False
        
        for n in c:
            is_odd |= n % 2
        
        return res + is_odd
