class Solution:
    def checkString(self, s: str) -> bool:
        last_a = 0
        first_b = len(s)
        
        for i, c in enumerate(s):
            if c == "a":
                last_a = i
            elif first_b == len(s):
                first_b = i
        
        return last_a <= first_b
