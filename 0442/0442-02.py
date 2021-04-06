class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            
            if nums[idx] < 0:
                ret.append(idx + 1)
                
            nums[idx] = -nums[idx]
            
        return ret
