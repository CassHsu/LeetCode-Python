class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}
        
        def chooseLastOne(nums):
            if len(nums) == 1:
                return nums

            if tuple(nums) in cache:
                return cache[tuple(nums)]
            
            max_t = []
            for i in range(0, len(nums) - 1):
                if nums[-1] % nums[i] == 0:
                    t = chooseLastOne(nums[:i+1])
                    if len(t) > len(max_t):
                        max_t = t
            max_t = [*max_t, nums[-1]]
            
            cache[tuple(nums)] = max_t
            return cache[tuple(nums)]
        
        max_l = []
        for i in range(len(nums)):
            l = chooseLastOne(nums[:i+1])
            if len(l) > len(max_l):
                max_l = l
        return max_l
