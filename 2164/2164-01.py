class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evens = sorted([nums[i] for i in range(0, n, 2)])
        odds = sorted([nums[i] for i in range(1, n, 2)], reverse=True)

        ans = []

        i, j = 0, 0
        while i < len(evens) or j < len(odds):
            if i < len(evens):
                ans.append(evens[i])
                i += 1
            if j < len(odds):
                ans.append(odds[j])
                j += 1
            
        return ans
