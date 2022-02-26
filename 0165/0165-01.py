class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split1 = version1.split('.')
        split2 = version2.split('.')
        
        n1 = len(split1)
        n2 = len(split2)
        
        for i in range(max(n1, n2)):
            i1 = int(split1[i]) if i < n1 else 0
            i2 = int(split2[i]) if i < n2 else 0
            
            if i1 != i2:
                return 1 if i1 > i2 else -1
            
        return 0
