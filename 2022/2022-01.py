class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        ans = []
        tmp = []
        
        for o in original:
            tmp.append(o)
            if len(tmp) == n:
                ans.append(tmp)
                tmp = []
        
        return ans
