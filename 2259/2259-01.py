class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        di = []
        
        for i, n in enumerate(number):
            if n == digit:
                di.append(i)
        
        res = []
        for i in di:
            res.append(int(number[:i] + number[i+1:]))
            
        return str(max(res))
