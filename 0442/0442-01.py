class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        m = {}
        ret = []
        for n in nums:
            if m.get(n) == None:
                m[n] = 1
            else:
                v = m.get(n)
                if v == 1:
                    ret.append(n)
                m[n] = v + 1
                
        return ret
