class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ns = [set(n) for n in nums]
        r = ns[0]
        for n in ns[1:]:
            r = r.intersection(n)
            
        return sorted(r)
