class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = s + t
        r = ord(st[0])
        for i in range(1, len(st)):
            r ^= ord(st[i])
        return chr(r)
