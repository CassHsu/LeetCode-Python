class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans = []
        counter = collections.Counter(arr1 + arr2 + arr3)
        
        for v, c in counter.items():
            if c == 3:
               ans.append(v)
            
        return ans
