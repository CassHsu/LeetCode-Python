class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        pv = arr[0]
        pi = 0
        
        for i in range(1, len(arr)):
            if arr[i] > pv:
                pv = arr[i]
                pi = i
        
        return pi
