class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        texts = text.split(" ")
        ans = len(texts)
        if brokenLetters == "":
            return ans
        
        for t in texts:
            for b in brokenLetters:
                if b in t:
                    ans -= 1
                    break
        
        return ans
