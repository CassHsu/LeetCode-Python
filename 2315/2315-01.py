class Solution:
    def countAsterisks(self, s: str) -> int:
        arr = s.split('|')
        count = 0
        
        for i in range(0, len(arr), 2):
            for c in arr[i]:
                if c == '*':
                    count += 1
                    
        return count
