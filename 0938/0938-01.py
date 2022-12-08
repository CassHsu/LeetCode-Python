class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      if not root:
        return 0

      v = 0
      if low <= root.val <= high:
        v = root.val

      l = self.rangeSumBST(root.left, low, high)
      r = self.rangeSumBST(root.right, low, high)

      return l + r + v
