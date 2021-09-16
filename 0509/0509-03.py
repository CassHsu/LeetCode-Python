class Solution:
    def fib(self, n: int) -> int:
        arr = [-1 if i >= 2 else i for i in range(n + 1)]
        
        def helper(x):
            if arr[x] != -1:
                return arr[x]
            
            v = helper(x - 1) + helper(x - 2)
            arr[x] = v
            return v
        
        return helper(n)
