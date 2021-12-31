class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for s in sentences:
            count = len(s.split(" "))
            if count > mx:
                mx = count
            
        return mx
