class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, h = 0, len(arr) - 1
        while l < h:
            m = int ((l + h) / 2)
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                h = m
        return l
