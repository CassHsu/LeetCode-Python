class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = list(s)
        st = list(t)
        ss.sort()
        st.sort()
        
        return ss == st
