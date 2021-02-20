class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        v = self.map.pop(key)
        self.map[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        elif len(self.map) >= self.capacity:
            del self.map[next(iter(self.map))]
        
        self.map[key] = value
