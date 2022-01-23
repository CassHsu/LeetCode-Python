class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s = {}
        for w in words1:
            if w not in s:
                s[w] = [1, 0]
            else:
                s[w][0] += 1
                
        for w in words2:
            if w not in s:
                s[w] = [0, 1]
            else:
                s[w][1] += 1
        
        count = 0
        for ls in s.values():
            if ls[0] == 1 and ls[1] == 1:
                count += 1
                
        return count
