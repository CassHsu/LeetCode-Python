class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or "" in strs: return ""
        if len(strs) == 1: return strs[0]
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].startswith(prefix) == False:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix