class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        nums = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                nums[i] = nums[i - 1] + 1
                
        if n > 1 and ratings[0] > ratings[1]:
            nums[0] = 2
            
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and nums[i] <= nums[i + 1]:
                nums[i] = nums[i + 1] + 1
                
        return sum(nums)
