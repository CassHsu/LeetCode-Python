class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = defaultdict(lambda: [])
        
        for i in range(len(paths)):
            p = paths[i]
            splits = p.split(' ')
            
            for j in range(1, len(splits)):
                s = splits[j].index('(')
                m[splits[j][s:]].append(splits[0] + '/' + splits[j][:s])
                
        return [m[i] for i in m if len(m[i]) > 1]
