class LRUCache:
    def __init__(self, capacity: int):
        self.map = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        value = self.map.pop(key)
        self.map[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        else:
            if len(self.map) >= self.capacity:
                self.map.popitem(last=False)
        self.map[key] = value
