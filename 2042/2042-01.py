class Solution:
    def areNumbersAscending(self, s: str) -> bool:              
        arr = [int(a) for a in s.split() if a.isnumeric()]
        
        for i in range(1, len(arr)):
            if arr[i - 1] >= arr[i]:
                return False
            
        return True
