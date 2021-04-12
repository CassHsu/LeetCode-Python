class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = [[]]
        start, end = 0, 0
        
        for i in range(len(nums)):
            start = 0
            
            if i > 0 and nums[i - 1] == nums[i]:
                start = end + 1
                
            end = len(ret) - 1
            for j in range(start, end + 1):
                ss = list(ret[j])
                ss.append(nums[i])
                ret.append(ss)
            
        return ret
