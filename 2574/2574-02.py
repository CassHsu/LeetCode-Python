class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]

        ls, rs = 0, sum(nums)
            
        for i, n in enumerate(nums):
            rs -= n
            ans[i] = abs(ls - rs)
            ls += n
            
        return ans
