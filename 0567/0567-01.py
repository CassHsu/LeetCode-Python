class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def match(c1, c2):
            for i in range(26):
                if c1[i] != c2[i]:
                    return False
            return True
        
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False
        
        counts = [0 for _ in range(26)]
        
        a = ord('a')
        for s in s1:
            counts[ord(s) - a] += 1
            
        for i in range(len_s2 - len_s1 + 1):
            compare = [0 for _ in range(26)]
            
            for j in range(len_s1):
                compare[ord(s2[i + j]) - a] += 1
                
            if match(counts, compare):
                return True
        
        return False
