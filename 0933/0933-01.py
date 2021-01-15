class RecentCounter:
    requests = []
    def __init__(self):
        self.requests = []    

    def ping(self, t: int) -> int:
        l = t -3000
        r = t
        self.requests.append(t)
        f = [x for x in self.requests if x <= r and x >= l]
        self.requests = f
        return len(f)