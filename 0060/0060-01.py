from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        ret = ""
        k -= 1
        
        while n > 0:
            n -= 1
            i, k = divmod(k, factorial(n))
            ret += str(nums[i])
            nums.remove(nums[i])
            
        return ret
