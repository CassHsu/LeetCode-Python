class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        dq = deque(tokens)
        
        ans = p = 0
        
        while dq and (power >= dq[0] or p):
            while dq and power >= dq[0]:
                power -= dq.popleft()
                p += 1
                
            ans = max(ans, p)
            
            if dq and p:
                power += dq.pop()
                p -= 1
        
        return ans
