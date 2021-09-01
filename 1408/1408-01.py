class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        
        for i, w in enumerate(words):
            if w in "@".join(words[i+1:]) or w in "@".join(words[:i]):
                ans.append(w)
        
        return ans
