class LRUCache:
    def __init__(self, capacity: int):
        self.deque = collections.deque()
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.deque.remove(key)
        self.deque.append(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deque.remove(key)
        elif len(self.map) >= self.capacity:
            k = self.deque.popleft()
            self.map.pop(k)
        
        self.deque.append(key)
        self.map[key] = value
