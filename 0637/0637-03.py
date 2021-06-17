class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ret = []
        q = [root]
        
        while q:
            ret.append(sum(n.val for n in q) / len(q))
            q = [t for n in q for t in [n.left, n.right] if t]
        
        return ret
