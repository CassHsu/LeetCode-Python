class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        
        for num in nums:
            for i in range(len(ret)):
                ss = list(ret[i])
                ss.append(num)
                ret.append(ss)
        
        return ret
