class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]

    def next(self) -> int:
        stack = self.stack
        val = stack.pop()
        if type(val) is int: return val
        right, left = val.right, val.left
        if right: stack.append(right)
        stack.append(val.val)
        if left: stack.append(left)
        return self.next()

    def hasNext(self) -> bool:
        return self.stack
