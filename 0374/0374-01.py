class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = floor(low + (high - low) / 2)
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1
