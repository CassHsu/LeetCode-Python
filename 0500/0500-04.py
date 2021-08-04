class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        return [w for w in words if any([all([c in row for c in w.lower()]) for row in rows])]
