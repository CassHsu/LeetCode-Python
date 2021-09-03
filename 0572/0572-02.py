class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def print_tree(node):
            if node:
                return f"R{node.val}{print_tree(node.left)}{print_tree(node.right)}"
            return "X"
        
        return print_tree(t) in print_tree(s)
