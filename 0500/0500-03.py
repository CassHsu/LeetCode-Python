class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [w for w in words if set(w).issubset(set("qwertyuiopQWERTYUIOP")) or set(w).issubset(set("asdfghjklASDFGHJKL")) or set(w).issubset(set("zxcvbnmZXCVBNM"))]
