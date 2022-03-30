class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        ans = nums[0]
        for k, v in counts.items():
            if v > 1:
                ans = k
                break
            
        return ans
