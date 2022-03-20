class FreqStack:

    def __init__(self):
        self.c = Counter()
        self.m = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.c[val] + 1
        self.c[val] = f
        
        if f > self.maxfreq:
            self.maxfreq = f
            
        self.m[f].append(val)

    def pop(self) -> int:
        val = self.m[self.maxfreq].pop()
        self.c[val] -= 1
        
        if not self.m[self.maxfreq]:
            self.maxfreq -= 1
            
        return val
