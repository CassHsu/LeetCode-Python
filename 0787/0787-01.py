def findCheapestPrice(n, flightMap, src, dst, K, cache):
    if K == -1:
        return -1
    
    if (src, K) in cache:
        return cache[(src, K)]
    
    minPrice = -1
    if src not in flightMap:
        return -1
    
    for d, p in flightMap[src]:
        if d == dst:
            if minPrice == -1 or p < minPrice:
                minPrice = p
        else:
            r = findCheapestPrice(n, flightMap, d, dst, K-1, cache)
            if r != -1:
                price = p + r
                if minPrice == -1 or price < minPrice:
                    minPrice = price
            
    cache[(src, K)] = minPrice
    return minPrice

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        flightMap = {}
        for s, d, p in flights:
            if s not in flightMap:
                flightMap[s] = []
            flightMap[s].append((d, p))
            
        cache = {}
        return findCheapestPrice(n, flightMap, src, dst, K, cache)
