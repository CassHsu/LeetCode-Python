class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.idx = 0
        self.count = 0
        self.vol = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.vol:
            return False
        
        self.q[(self.idx + self.count) % self.vol] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        
        self.idx = (self.idx + 1) % self.vol
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        
        return self.q[self.idx]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        
        return self.q[(self.idx + self.count - 1) % self.vol]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.vol
