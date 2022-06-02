class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        ans = []
        
        for n in nums:
            acc += n
            ans.append(acc)
        
        return ans
