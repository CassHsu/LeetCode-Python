class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s_arr = sorted(arr, key = lambda n: abs(x - n))
        
        res = []
        for i in range(k):
            res.append(s_arr[i])
            
        return sorted(res)
