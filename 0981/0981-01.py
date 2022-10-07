class TimeMap:
    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.m:
            self.m[key] = {}
            
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.m:
            return ''
        
        for t in reversed(range(1, timestamp + 1)):
            if t in self.m[key]:
                return self.m[key][t]
            
        return ''
