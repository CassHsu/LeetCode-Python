class Solution:
    def maxProduct(self, words: List[str]) -> int:
        counts = []
        for w in words:
            c = Counter(w)
            counts.append(c)
            
        ans = 0
        n = len(words)
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    c1 = counts[i]
                    c2 = counts[j]
                    find = False
                    
                    for k in range(26):
                        c = chr(ord('a') + k)
                        if c1[c] and c2[c]:
                            find = True
                            break
                            
                    if not find:
                        ans = max(ans, len(words[i]) * len(words[j]))
        return ans
