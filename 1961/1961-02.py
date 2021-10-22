class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        count = 0
        for word in words:
            if count + len(word) > len(s):
                break
                
            for w in word:
                if w != s[count]:
                    return False
                
                count += 1
                
        return count == len(s)
