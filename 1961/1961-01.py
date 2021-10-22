class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i, count = 0, 0
        
        while i < len(words):
            count += len(words[i])
            
            if len(s) == count:
                return s[0] == words[0][0] and s[-1] == words[i][-1]
            
            i += 1
            
        return False
