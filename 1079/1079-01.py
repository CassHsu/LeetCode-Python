class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        
        def backtrack(t, curr, idx):
            if idx == len(curr):
                ans.add(curr)
                return
            
            for i in range(len(t)):
                backtrack(t[:i] + t[i+1:] , curr + t[i], idx)
                    
        for i in range(1, len(tiles) + 1):
            backtrack(tiles, "", i)
         
        return len(ans)
