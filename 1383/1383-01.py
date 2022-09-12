class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for e, s in zip(efficiency, speed):
            eng.append([e, s])
            
        eng.sort(reverse=True)
        
        res, speed = 0, 0
        min_heap = []
        
        for e, s in eng:
            if len(min_heap) == k:
                speed -= heapq.heappop(min_heap)
                
            speed += s
            heapq.heappush(min_heap, s)
            res = max(res, e * speed)
            
        return res % (10 ** 9 + 7)
