class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        pairs = set()

        for w in words:
            rw = w[::-1]
            if w != rw and rw in words and rw not in pairs:
                count += 1
                pairs.add(w)
                
        return count
