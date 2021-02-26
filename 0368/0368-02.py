class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {0: [nums[0]]}
        
        def chooseLastOne(nums, lastIndx):
            if lastIndx in cache:
                return cache[lastIndx]
            
            max_t = []
            for i in range(0, lastIndx):
                if nums[lastIndx] % nums[i] == 0:
                    t = chooseLastOne(nums, i)
                    if len(t) > len(max_t):
                        max_t = t
            max_t = [*max_t, nums[lastIndx]]
            
            cache[lastIndx] = max_t
            return cache[lastIndx]
        
        max_l = []
        for i in range(len(nums)):
            l = chooseLastOne(nums, i)
            if len(l) > len(max_l):
                max_l = l
        return max_l
