from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = []
        m = defaultdict(list)
        for src, des in sorted(tickets)[::-1]:
            m[src].append(des)
            
        stack = ['JFK']
        while stack:
            while m[stack[-1]]:
                stack.append(m[stack[-1]].pop())
            path.append(stack.pop())
            
        return path[::-1]
