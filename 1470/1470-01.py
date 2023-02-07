class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_1 = nums[:n]
        nums_2 = nums[n:]
        ans = []
        
        for i in range(len(nums_1)):
            ans.append(nums_1[i])
            ans.append(nums_2[i])

        return ans
