class Solution:
    def reverse(self, x: int) -> int:
        lb = pow(-2, 31)
        ub = pow(2, 31) - 1
        
        if lb >= x and x > ub:
            return 0
        
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x
            
        ans = -int(str(x)[::-1]) if is_negative else int(str(x)[::-1])
        
        
        if lb < ans and ans < ub:
            return ans
        else:
            return 0
