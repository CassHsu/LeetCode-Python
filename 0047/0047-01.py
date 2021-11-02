from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        prem = []
        count = Counter(nums)
            
        def backtracking():
            if len(prem) == len(nums):
                res.append(prem.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    prem.append(n)
                    count[n] -= 1
                    
                    backtracking()
                    
                    count[n] += 1
                    prem.pop()
                    
        backtracking()
        return res
