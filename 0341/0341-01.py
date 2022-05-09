class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))
        
    def next(self) -> int:
        self.extend_stack_top_i()
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        self.extend_stack_top_i()
        return len(self.stack) > 0

    def extend_stack_top_i(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))
