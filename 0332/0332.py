from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = []
        m = defaultdict(list)
        for src, des in sorted(tickets)[::-1]:
            m[src].append(des)
            
        def dfs(port):
            while m[port]:
                dfs(m[port].pop())
            path.append(port)
        
        dfs('JFK')
        return path[::-1]
