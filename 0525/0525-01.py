class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        m = { 0: -1 }
        
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                count -= 1
                
            if count in m.keys():
                ans = max(ans, i - m[count])
            else:
                m[count] = i
        
        return ans
