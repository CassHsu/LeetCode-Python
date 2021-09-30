class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        while True:
            mid = (start + end) // 2
            
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
                
        return mid
