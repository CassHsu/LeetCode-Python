class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = []
        subsets = [0]
        for n in nums:
            tmp = subsets.copy()
            for s in subsets:
                # print(subsets, s, n, s ^ n)
                tmp.append(s ^ n)
                result.append(tmp[-1])
            subsets = tmp
            # print(subsets)
        
        return sum(result)
