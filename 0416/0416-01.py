class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        target = sum_nums // 2
        
        for i in range(len(nums)):
            newDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                
                newDP.add(t + nums[i])
                newDP.add(t)
                
            dp = newDP
            
        return True if target in dp else False
