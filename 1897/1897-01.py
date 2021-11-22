from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter(''.join(words))
        size = len(words)
        return all([c % size == 0 for c in counts.values()])
