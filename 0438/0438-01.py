class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = {}, {}
        
        for c in p:
            if need.get(c):
                need[c] += 1
            else:
                need[c] = 1
            
        left, right = 0, 0
        valid = 0
        res = []
        
        while right < len(s):
            c = s[right]
            right += 1
            
            if need.get(c):
                if window.get(c):
                    window[c] += 1
                else:
                    window[c] = 1
                    
                if window[c] == need[c]:
                    valid += 1
            
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)

                c = s[left]
                left += 1

                if need.get(c):
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
                
        return res
