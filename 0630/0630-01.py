class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        courses.sort(key = lambda x: x[1])
        t = 0
        
        for d, end in courses:
            heappush(heap, -d)
            t += d
            
            while t > end:
                t += heappop(heap)
                
        return len(heap)
