class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        
        multiply = original * 2
        while multiply in nums:
            multiply *= 2
            
        return multiply
