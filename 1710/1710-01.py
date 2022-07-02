class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        
        for box_num, num_units in boxTypes:
            if truckSize < box_num:
                return ans + num_units * truckSize
            
            ans += num_units * box_num
            truckSize -= box_num
        
        return ans
