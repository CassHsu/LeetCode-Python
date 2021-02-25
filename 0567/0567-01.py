class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        lenS2 = len(s2)
        
        if (lenS1 > lenS2):
            return False
    
        countS1 = [0 for _ in range(26)]
        for i in range(lenS1):
            countS1[ord(s1[i]) - ord('a')] += 1
            
        for i in range(lenS2 - lenS1 + 1):
            countS2 = [0 for _ in range(26)]
            for j in range(lenS1):
                countS2[ord(s2[i + j]) - ord('a')] += 1
                
            if self.match(countS1, countS2):
                return True
    
        return False
    
    def match(self, c1, c2):
        for i in range(26):
            if c1[i] != c2[i]:
                return False
        return True
