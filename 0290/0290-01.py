class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        
        if len(pattern) != len(words):
            return False
        
        p_m = {}
        w_m = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in p_m:
                p_m[pattern[i]] = words[i]
            else:
                if p_m[pattern[i]] != words[i]:
                    return False
                
            if words[i] not in w_m:
                w_m[words[i]] = pattern[i]
            else:
                if w_m[words[i]] != pattern[i]:
                    return False
            
        return True
