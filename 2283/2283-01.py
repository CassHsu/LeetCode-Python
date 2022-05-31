class Solution:
    def digitCount(self, num: str) -> bool:
        nums = [int(n) for n in num]
        c = Counter(nums)
        
        for i, n in enumerate(nums):
            if c[i] != n:
                return False
            
        return True
