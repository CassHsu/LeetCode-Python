class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        keep = word
        while word in sequence:
            count += 1
            word += keep
            
        return count