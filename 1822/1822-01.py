class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for n in nums:
            p *= n
            
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        
        return signFunc(p)
