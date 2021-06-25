class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(n for n in nums if n % 2 == 0)
        ans = []
        
        for k, i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]
                
            nums[i] += k
            
            if nums[i] % 2 == 0:
                s += nums[i]
                
            ans.append(s)
                
        return ans
