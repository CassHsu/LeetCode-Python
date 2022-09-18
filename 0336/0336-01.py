class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        m = {}
        for i, w in enumerate(words):
            m[w] = i
            
        res = set()
        for i, w in enumerate(words):
            if not w:
                continue
            
            for j in range(len(w)):
                curr = w[:j]
                t = w[j:][::-1]
                if curr == curr[::-1] and t != w and t in m:
                    res.add((m[t], i))
                    
            for j in range(len(w), -1, -1):
                curr = w[j:]
                t= w[:j][::-1]
                if curr == curr[::-1] and t != w and t in m:
                    res.add((i, m[t]))
                    
            if w == w[::-1] and "" in m:
                x = m[""]
                res.add((i, x))
                res.add((x, i))

        return list(res)
