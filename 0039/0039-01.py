class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def backtrack(idx, curr):
            total = sum(curr)
            
            if total == target:
                ret.append(curr[:])
            
            for i in range(idx, len(candidates)):
                if total + candidates[i] > target:
                    return
                
                curr.append(candidates[i])
                backtrack(i, curr)
                curr.pop()
        
        candidates.sort()
        backtrack(0, [])
        return ret
