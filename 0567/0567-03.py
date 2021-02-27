class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = "".join(sorted(s1))
        curr = ""
        
        for c in s2:
            curr += c
            if len(curr) == len(s1):
                if "".join(sorted(curr)) == target:
                    return True
                curr = curr[1:]
        return False
