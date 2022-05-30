class Solution:
    def common_letter(self, w1, w2):
        for w in w1:
            if w in w2:
                return True
        return False
    
    def maxProduct(self, words: List[str]) -> int:
        p = 0
        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                if not self.common_letter(words[i], words[j]):
                    p = max(p, len(words[i]) * len(words[j]))
        
        return p
