class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum([1 for w in words if w == s[:len(w)]])
