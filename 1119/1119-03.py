class Solution:
    def removeVowels(self, s: str) -> str:
        m = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}

        return ''.join([c for c in s if c not in m])
