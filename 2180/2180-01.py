class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        
        for n in range(1, num + 1):
            if n < 10:
                if n % 2 == 0:
                    count += 1
                    
            else:
                ns = str(n)
                x = 0
                for s in ns:
                    x += int(s)
                
                if x % 2 == 0:
                    count += 1
                                
        return count
