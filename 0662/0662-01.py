class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        q = deque()
        q.append((root, 0))

        while q:
            lvl = len(q)
            _, level_head_index = q[0]

            for _ in range(lvl):
                node, i = q.popleft()
                if node.left:
                    q.append((node.left, 2 * i))
                if node.right:
                    q.append((node.right, 2 * i + 1))

            max_width = max(max_width, i - level_head_index + 1)

        return max_width
