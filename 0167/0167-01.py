class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        
        for i, n in enumerate(numbers):
            if n in m:
                return [m[n] + 1, i + 1]
            else:
                m[target - n] = i
        
        return [-1, -1]
