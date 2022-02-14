class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr, ret, start):
            ret.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(nums, curr, ret, i + 1)
                curr.pop()
            
        
        ret = []
        backtrack(nums, [], ret, 0)
        return ret
