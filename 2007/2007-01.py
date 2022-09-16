class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        ans = []
        
        if len(changed) % 2:
            return ans
        
        for c in sorted(count.keys()):
            if count[c] > count[c * 2]:
                return []
            
            if c == 0:
                if count[c] % 2:
                    return []
                else:
                    ans += [0] * (count[c] // 2)
            else:
                ans += count[c] * [c]
            
            count[c * 2] -= count[c]
            
        return ans
