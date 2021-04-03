class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        left, right = 0, size
        
        while left < right:
            mid = (left + right)//2
            
            h = size - mid
            
            if citations[mid] >= h:
                right = mid
            else:
                left = mid + 1
                
        return size - right
