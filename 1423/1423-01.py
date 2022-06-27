class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l, r = 0, n - k
        
        total = sum(cardPoints[r:])
        ans = total
        
        while r < n:
            total += (cardPoints[l] - cardPoints[r])
            ans = max(ans, total)
            l += 1
            r += 1
            
        return ans
