class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        last = 0
        largest = 0
        for g in gain:
            last = last + g
            if last > largest:
                largest = last
            
        return largest
