class Solution:
    def reverseVowels(self, s: str) -> str:
        res = [c for c in s]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        l, r = 0, len(s) - 1
        while l < r:
            if res[l] in vowels and res[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            elif res[l] not in vowels:
                l += 1
            else:
                r -= 1

        return ''.join(res)
