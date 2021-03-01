class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        h = [-x for x in stones]
        heapq.heapify(h)
        
        while len(h) > 1:
            y = heapq.heappop(h)
            x = heapq.heappop(h)
            
            if y != x:
                heapq.heappush(h, y - x)
                
        if len(h) == 0:
            return 0
        else:
            return -h[0]
