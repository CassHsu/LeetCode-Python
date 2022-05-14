class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        combi = []
        for i in range(1, len(s) + 1):
            combi.append(s[:i])
            
        count = 0
        for w in words:
            if w in combi:
                count += 1
                
        return count
