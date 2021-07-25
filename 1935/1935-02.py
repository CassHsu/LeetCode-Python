class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        def checker(w):
            return all([i not in brokenLetters for i in set(w)])
        
        return len([True for w in text.split(" ") if checker(w)])
