class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        m = {'0': [], '1': [], '2': [],
             '3': [], '4': [], '5': [],
             '6': [], '7': [], '8': [], '9': []}
        
        for i in range(1, len(rings), 2):
            m[rings[i]].append(rings[i-1])
        
        for rod in m.values():
            r = False
            g = False
            b = False
            
            for v in rod:
                if v == 'R':
                    r = True
                elif v == 'G':
                    g = True
                elif v == 'B':
                    b = True
                    
                if r and g and b:
                    count += 1
                    break
        
        return count
