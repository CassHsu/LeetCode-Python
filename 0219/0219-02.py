class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ks = set()
        for i, n in enumerate(nums):
            if n in ks:
                return True
            ks.add(n)
            if len(ks) > k:
                ks.remove(nums[i-k])
                
        return False
