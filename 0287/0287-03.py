class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        
        ans = 0
        for n in nums:
            if n in seen:
                ans = n
                break
            
            seen.add(n)
            
        return ans
