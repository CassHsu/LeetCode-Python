class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1, min2, max2, max1 = float('inf'), float('inf'), 0, 0
        
        for n in nums:
            if n <= min1: 
                min2 = min1
                min1 = n
                
            elif n <= min2: 
                min2 = n
            
            if max1 <= n:
                max2 = max1
                max1 = n
                
            elif max2 <= n:
                max2 = n
                
        return max2 * max1 - min1 * min2
