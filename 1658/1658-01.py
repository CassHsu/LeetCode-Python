class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        curr = sum(nums)
        n = len(nums)
        mini = inf
        l = 0
        
        for r in range(n):
            curr -= nums[r]
            while curr < x and l <= r:
                curr += nums[l]
                l += 1
                
            if curr == x:
                mini = min(mini, (n - 1 - r) + l)
                
        return mini if mini != inf else -1
