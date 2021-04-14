class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if n in m.keys():
                m[n] += 1
            else:
                m[n] = 1
                
        ans = 0
        for k, v in m.items():
            if v == 1:
                ans += k
                
        return ans
