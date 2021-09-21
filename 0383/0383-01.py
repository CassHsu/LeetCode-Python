class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        m = defaultdict(int)
        
        for c in magazine:
            m[c] += 1
            
        for c in ransomNote:
            if c not in m:
                return False
            
            m[c] -= 1
            if m[c] < 0:
                return False
        
        return True
