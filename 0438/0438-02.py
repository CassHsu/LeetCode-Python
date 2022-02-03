class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        
        if s_len < p_len:
            return []
        
        ans = []
        p_count = [0] * 26
        s_count = [0] * 26
        
        a = ord('a')
        for c in p:
            p_count[ord(c) - a] += 1
            
        for i in range(s_len):
            s_count[ord(s[i]) - a] += 1
            if i >= p_len:
                s_count[ord(s[i - p_len]) - a] -= 1
                
            if p_count == s_count:
                ans.append(i - p_len + 1)
         
        return ans
