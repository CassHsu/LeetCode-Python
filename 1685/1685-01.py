class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        size = len(nums)
        
        curr = 0
        result = []
        
        for i, n in enumerate(nums):
            curr += n
            result.append((i+1)*n - curr + (total - curr)-(size-i-1) * n)
        
        return result
