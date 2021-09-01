class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        w_str = " ".join(words)
        return [w for w in words if w_str.count(w) >= 2]
