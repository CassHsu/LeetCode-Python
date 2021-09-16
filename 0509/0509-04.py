class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        prev, last = 0, 1
        
        for _ in range(2, n):
            prev, last = last, prev + last
            
        return prev + last
