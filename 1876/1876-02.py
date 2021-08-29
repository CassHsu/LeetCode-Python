class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        bucket = []
        
        for i in range(len(s)):
            if i < len(s) - 2:
                bucket.append(s[i:i+3])
            
        count = 0
        for b in bucket:
            is_1 = True
            for v in Counter(b).values():
                if v > 1:
                    is_1 = False
                    break
                    
            if is_1:
                count += 1
                
        return count
