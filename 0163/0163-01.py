class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def append(low, high):
            if low + 2 == high:
                ans.append(str(low + 1))
            else:
                ans.append(f'{low + 1}->{high - 1}')
            
        ans = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                append(nums[i - 1], nums[i])
        
        return ans
