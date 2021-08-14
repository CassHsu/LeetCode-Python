class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(curr):
            nonlocal ans, nums
            if len(curr) == len(nums):
                ans.append(list(curr))
                return
            
            for n in nums:
                if n in curr:
                    continue
                
                curr.append(n)
                backtrack(curr)
                curr.pop()
        
        backtrack([])
        return ans
