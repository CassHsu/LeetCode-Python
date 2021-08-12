class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr, ret, i):
            if i == len(nums):
                ret.append(curr[:])
                return
            
            backtrack(nums, curr, ret, i + 1)
            curr.append(nums[i])
            backtrack(nums, curr, ret, i + 1)
            curr.remove(curr[-1])
                
        
        ret = []
        backtrack(nums, [], ret, 0)
        return ret
