class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_d = len(wordsDict)
        p1, p2 = -1, -1
        
        for i, w in enumerate(wordsDict):
            if w == word1:
                p1 = i
            elif w == word2:
                p2 = i
                
            if p1 != -1 and p2 != -1:
                min_d = min(min_d, abs(p1 - p2))
                
        return min_d
