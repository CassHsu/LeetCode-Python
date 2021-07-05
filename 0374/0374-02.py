class Solution:
    def guessNumber(self, n: int) -> int:
        h = floor(n / 2)
        r = guess(h)
        
        while (True):
            if r > 0:
                h = floor((h + 1 + n) / 2)
                r = guess(h)
            elif r < 0:
                n = h
                h = floor((1 + h) / 2)
                r = guess(h)
            else:
                return h
        return h
