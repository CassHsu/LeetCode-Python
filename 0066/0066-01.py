class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = int("".join(str(s) for s in digits)) + 1
        
        return [s for s in str(d)]
