class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 and right == 0:
            return 0
        elif len(bin(left)) != len(bin(right)):
            return 0
        else:
            l = bin(left)[2:]
            r = bin(right)[2:]
            
            for i in range(len(r)):
                if l[i] != r[i]:
                    l = l[:i] + ("0" * len(r[i:]))
                    break
                    
            return int(l, 2)
