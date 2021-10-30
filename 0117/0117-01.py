class Solution:
    def connect(self, root: 'Node') -> 'Node':
        levels = defaultdict(list)

        def inorder(node, lvl):
            if not node:
                return

            levels[lvl].append(node)
            inorder(node.left, lvl+1)
            inorder(node.right, lvl+1)

        inorder(root, 0)

        def dfs(node, lvl):
            if not node:
                return None

            idx = levels[lvl].index(node)

            if idx != len(levels[lvl]) - 1:
                node.next = levels[lvl][idx+1]

            node.left = dfs(node.left, lvl+1)
            node.right = dfs(node.right, lvl+1)

            return node

        return dfs(root,0)
