class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c = Counter()
        for i in range(1, len(nums)):
            if nums[i - 1] == key:
                c[nums[i]] += 1
                
        return c.most_common(1)[0][0]
