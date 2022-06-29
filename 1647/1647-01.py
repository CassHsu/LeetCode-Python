class Solution:
    def minDeletions(self, s: str) -> int:
        count = 0
        counter = Counter(s)
        freq = sorted(counter.values())[::-1]
        
        for i in range(len(freq)):
            while freq[i] != 0 and freq[i] in freq[:i] + freq[i + 1:]:
                freq[i] -= 1
                count += 1
            
        return count
