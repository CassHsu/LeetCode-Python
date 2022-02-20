class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, -n * 2 if n % 2 else -n)
            
        ans = float('inf')
        mi = -max(pq)
        while len(pq) == len(nums):
            n = -heapq.heappop(pq)
            ans = min(ans, n - mi)
            if n % 2 == 0:
                mi = min(mi, n / 2)
                heapq.heappush(pq, -n / 2)
                
        return int(ans)
