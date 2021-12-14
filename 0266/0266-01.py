from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        counter = Counter(s)
        
        for v in counter.values():
            count += v % 2
        
        return count <= 1
