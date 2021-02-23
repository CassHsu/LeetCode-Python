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
            if isBadVersion(mid) and isBadVersion(mid - 1) == False:
                return mid
            
            if isBadVersion(mid) == False:
                start = mid + 1
            else:
                end = mid
        return 0
