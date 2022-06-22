class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        alloc = []
        
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            
            if climb <= 0:
                continue
                
            heapq.heappush(alloc, climb)
            
            if len(alloc) <= ladders:
                continue
                
            bricks -= heapq.heappop(alloc)
            
            if bricks < 0:
                return i
            
        return len(heights) - 1
