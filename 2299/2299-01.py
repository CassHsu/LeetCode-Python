class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        lowers = 'abcdefghijklmnopqrstuvwxyz'
        uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '1234567890'
        specials = '!@#$%^&*()-+'
        
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        
        for i in range(len(password)):
            if not has_lower and password[i] in lowers:
                has_lower = True
                
            if not has_upper and password[i] in uppers:
                has_upper = True
                
            if not has_digit and password[i] in digits:
                has_digit = True
                
            if not has_special and password[i] in specials:
                has_special = True
                
            if i > 0 and password[i] == password[i - 1]:
                return False
        
        return has_lower and has_upper and has_digit and has_special
