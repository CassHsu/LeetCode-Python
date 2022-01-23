class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        c1 = Counter(words1)
        c2 = Counter(words2)
        
        for k in c1:
            if c1.get(k, 0) == 1 and c2.get(k, 0) == 1:
                count += 1
                
        return count
