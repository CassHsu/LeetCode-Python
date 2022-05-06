class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            item = self.stack[-1]
            self.stack = self.stack[:len(self.stack) - 1]
            return item
        else:
            return None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else None
