class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        i = 1
        target = 0
        while count < k:
            if i not in arr:
                target = i
                count += 1
                
            i += 1
            
        return target
