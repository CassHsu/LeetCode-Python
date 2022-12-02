class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        h = int(len(s) / 2)
        a = s[:h]
        b = s[h:]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        return len([x for x in a if x in vowels]) == len([x for x in b if x in vowels])
