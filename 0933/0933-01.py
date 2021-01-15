class RecentCounter:
    requests = []
    def __init__(self):
        self.requests = []    

    def ping(self, t: int) -> int:
        l = t -3000
        self.requests.append(t)
        self.requests  = [x for x in self.requests if x >= l]
        return len(self.requests)