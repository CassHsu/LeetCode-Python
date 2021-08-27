class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        m = {}
        
        for n in nums:
            if n not in m:
                m[n] = 1
            else:
                m[n] += 1
                
        for k, v in m.items():
            if v == 1:
                ans = k
                break
        
        return ans
