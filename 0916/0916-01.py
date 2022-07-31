class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for w in word:
                ans[ord(w) - ord('a')] += 1
            return ans
        
        mx2 = [0] * 26
        for w in words2:
            for i, c in enumerate(count(w)):
                mx2[i] = max(mx2[i], c)
                
        ans = []
        for w in words1:
            if all(x >= y for x, y in zip(count(w), mx2)):
                ans.append(w)
                
        return ans
