class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        return min(abs(i - j) for i, w1 in enumerate(wordsDict) if w1 == word1 for j, w2 in enumerate(wordsDict) if w2 == word2)
