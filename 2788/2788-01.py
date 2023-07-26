class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            res += [w for w in word.split(separator) if len(w) > 0]

        return res
