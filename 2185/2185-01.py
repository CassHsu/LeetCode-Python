class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        p = len(pref)
        for w in words:
            if w[:p] == pref:
                count += 1
                
        return count
