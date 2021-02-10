class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0: return [0]
        if num == 1: return [1]
        
        r = 2
        res = [0, 1]
        while r <= num:
            count = 0
            for n in bin(r)[2:]:
                if n == "1":
                    count += 1
            
            res.append(count)
            r += 1
            
        return res