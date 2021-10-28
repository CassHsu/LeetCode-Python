from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        total, count = 0, 0
        
        for c in counter:
            if counter[c] % 2 == 0:
                total += counter[c]
            else:
                total += counter[c] - 1
                count += 1
                
        return total if count == 0 else total + 1
