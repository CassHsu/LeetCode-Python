class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        m = {}
        
        def find(x):
            m.setdefault(x, x)
            if x != m[x]:
                m[x] = find(m[x])
            
            return m[x]
        
        def union(x, y):
            m[find(x)] = find(y)
            
        for e in equations:
            if e[1] == '=':
                union(e[0], e[-1])
                
        for e in equations:
            if e[1] == '!':
                if find(e[0]) == find(e[-1]):
                    return False
                
        return True
