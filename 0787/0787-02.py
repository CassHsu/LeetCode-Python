class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        prices = collections.defaultdict(dict)
        for s, d, p in flights:
            prices[s][d] = p
            
        heap = [(0, src, K + 1)]
        while heap:
            p, s, k = heapq.heappop(heap)
            if s == dst:
                return p
            if k > 0:
                for d in prices[s]:
                    heapq.heappush(heap, (p + prices[s][d], d, k - 1))
        return -1
