class RecentCounter:
    def __init__(self):
        self.requests = deque()  

    def ping(self, t: int) -> int:
        l = t -3000
        self.requests.append(t)
        
        while self.requests[0] < l:
            self.requests.popleft()
        
        return len(self.requests)