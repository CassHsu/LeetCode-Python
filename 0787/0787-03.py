class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        q = collections.deque()
        minp = float('inf')
        
        for s, d, p in flights:
            graph[s].append((p, d))
		
        q.append((src, 0, 0))
        while q:
            s, d, p = q.popleft()
            if s == dst:
                minp = min(minp, p)
                continue

            if d <= K and p <= minp:
                for r, n in graph[s]:
                    q.append((n, d+1, p + r))
                                
        return minp if minp!=float('inf') else -1
