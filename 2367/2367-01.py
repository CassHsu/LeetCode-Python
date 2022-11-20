class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set()
        count = 0
        
        for n in nums:
            if (n - diff) in s and (n - diff - diff) in s:
                count += 1
            s.add(n)

        return count
