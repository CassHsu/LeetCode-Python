class MinStack:
    def __init__(self):
        self.stack = []
        self.minlist = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minlist) > 0 and x > self.minlist[-1]:
            self.minlist.append(self.minlist[-1])
        else:
            self.minlist.append(x)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minlist = self.minlist[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minlist[-1]
