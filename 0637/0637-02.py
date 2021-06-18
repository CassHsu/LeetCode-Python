from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        counts = defaultdict(int)
        sums = defaultdict(int)
        
        def dfs(n, i):
            if not n:
                return
            
            counts[i] += 1
            sums[i] += n.val
            dfs(n.left, i+1)
            dfs(n.right, i+1)
            
        dfs(root, 0)
        return [sums[i] / counts[i] for i in range(len(counts))]
