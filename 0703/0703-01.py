class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        self.heappop()

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.heappop()
            
        return self.heap[0]
    
    def heappop(self):
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
