class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        ans.append(first)
        for e in encoded:
            ans.append(e ^ ans[-1])
            
        return ans