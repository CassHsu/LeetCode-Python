class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[0]
        self.stack.remove(x)
        return x
        

    def peek(self) -> int:
        return 0 if len(self.stack) == 0 else self.stack[0]
        

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False
