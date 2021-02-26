class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = [None] * len(nums)
        cache[0] = [nums[0]]
        max_cache = cache[0]
        
        for lastIndx in range(1, len(nums)):
            max_t = []
            for i in range(0, lastIndx):
                if nums[lastIndx] % nums[i] == 0:
                    t = cache[i]
                    if len(t) > len(max_t):
                        max_t = t
            max_t = [*max_t, nums[lastIndx]]
            cache[lastIndx] = max_t
        
            if len(cache[lastIndx]) > len(max_cache):
                max_cache = cache[lastIndx]
                
        return max_cache
