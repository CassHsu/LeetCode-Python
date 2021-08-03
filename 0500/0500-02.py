class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        lower_words = [word.lower() for word in words]
        ans = []
        
        for i, word in enumerate(lower_words):
            counts = [0, 0, 0]
            for w in word:
                for j, row in enumerate(rows):
                    if w in row:
                        counts[j] += 1
                
            for j in range(3):
                if counts[j] == len(word):
                    ans.append(words[i])
                    break
            
        return ans
