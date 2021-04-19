class Solution:
    def minOperations(self, nums: List[int]) -> int:        
        count = 0
        prev = 0
        for n in nums:
            if n <= prev:
                prev += 1
                count += prev - n
            else:
                prev = n
        return count
