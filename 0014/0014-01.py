class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        minLen = min([len(s) for s in strs])
        end = 0
        while end < minLen:
            for i in range(1, len(strs)):
                if strs[i - 1][end] != strs[i][end]:
                    return strs[0][:end]
            end += 1
            
        return strs[0][:end]