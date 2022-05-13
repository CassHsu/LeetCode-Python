class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                res.append(list(comb))
                return
            
            for n in counter:
                if counter[n] > 0:
                    comb.append(n)
                    counter[n] -= 1
                    
                    backtrack(comb, counter)
                    
                    comb.pop()
                    counter[n] += 1
        
        backtrack([], Counter(nums))
        return res
