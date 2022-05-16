class Solution:
    lvlsum = 0
    maxlvl = 0
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.lvlsum
        
    def dfs(self, root, lvl):
        if not root:
            return
        if lvl > self.maxlvl:
            self.maxlvl, self.lvlsum = lvl, root.val
        elif lvl == self.maxlvl:
            self.lvlsum += root.val
            
        self.dfs(root.left, lvl+1)
        self.dfs(root.right, lvl+1)
