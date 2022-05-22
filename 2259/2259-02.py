class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = -1
        
        for i, n in enumerate(number):
            if n == digit:
                res = max(res, int(number[:i] + number[i + 1:]))
                
        return str(res)
