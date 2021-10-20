class Solution:
    def areNumbersAscending(self, s: str) -> bool:        
        def check(x):
            try:
                int(x)
                return True
            except:
                return False
        
        arr = [int(a) for a in s.split() if check(a)]
        
        for i in range(1, len(arr)):
            if arr[i - 1] >= arr[i]:
                return False
            
        return True
