class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        ans = [-1, -1]
        
        for i in range(1, len(nums) + 1):
            if ctr[i] == 2:
                ans[0] = i
                
            if ctr[i] == 0:
                ans[1] = i
        
        return ans
