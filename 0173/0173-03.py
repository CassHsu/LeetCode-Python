class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def inorder(n):
            if n:
                inorder(n.left)
                self.nodes.append(n.val)
                inorder(n.right)
        
        self.nodes = deque()
        inorder(root)

    def next(self) -> int:
        return self.nodes.popleft()

    def hasNext(self) -> bool:
        return True if self.nodes else False
