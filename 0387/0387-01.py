from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(list(s))
        uniqChars = [item[0] for item in counter.items() if item[1] == 1]
        for i, c in enumerate(s):
            if c in uniqChars:
                return i
        return -1