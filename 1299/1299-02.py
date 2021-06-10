class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        maximum = arr[-1]
        arr[-1] = -1
        
        for i in range(size-2, -1, -1):
            tmp = maximum
            maximum = arr[i] if arr[i] > maximum else maximum
            arr[i] = tmp
        
        return arr
