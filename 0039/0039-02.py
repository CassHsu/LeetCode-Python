class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def backtrack(currentCandidates=candidates, remain=target, curr=[]):
            if remain < 0:
                return
            if remain == 0:
                ret.append(curr)
                return
        
            for i, c in enumerate(currentCandidates):
                backtrack(currentCandidates[i:], remain - c, curr + [c])
                
        backtrack()
        return ret;
