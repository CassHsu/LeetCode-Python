class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def matches(arr1, arr2):
            for i in range(26):
                if arr1[i] != arr2[i]:
                    return False
            return True
        
        size1 = len(s1)
        size2 = len(s2)
        
        if (size1 > size2):
            return False
        
        a = ord('a')
        arr1 = [0] * 26
        arr2 = [0] * 26
        for i in range(size1):
            arr1[ord(s1[i]) - a] += 1
            arr2[ord(s2[i]) - a] += 1
            
        w = size2 - size1
        for i in range(w):
            if matches(arr1, arr2):
                return True
            
            arr2[ord(s2[i + size1]) - a] += 1
            arr2[ord(s2[i]) - a] -= 1
        
        return matches(arr1, arr2)
