class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums) // 2
        counter = Counter(nums)
        
        count = 0
        for v in counter.values():
            if v % 2 == 0:
                count += (v / 2)
            
        return count == n
