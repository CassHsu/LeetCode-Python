import re

class Solution:
    def reformat(self, s: str) -> str:
        alpha, digit = [], []
        
        for c in s:
            if re.match('[0-9]', c):
                digit.append(c)
            else:
                alpha.append(c)
                
        if abs(len(alpha) - len(digit)) > 1:
            return ""
        
        z = None
        if len(digit) > len(alpha):
            alpha.append("")
            z = zip(digit, alpha)
        elif len(alpha) > len(digit):
            digit.append("")
            z = zip(alpha, digit)
        else:
            z = zip(alpha, digit)
        
        z = list(z)
        return "".join(list(map(lambda x: x[0] + x[1], z)))
