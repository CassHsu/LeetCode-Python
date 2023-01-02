class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        size = len(words)
        ws = set()
        if size != len(pattern):
            return False

        m = collections.defaultdict(str)

        for i, p in enumerate(pattern):
            for _ in range(i, size):
                if p in m:
                    if m[p] != words[i]:
                        return False
                else:
                    if words[i] in ws:
                        return False

                    m[p] = words[i]
                    ws.add(words[i])

        return True
