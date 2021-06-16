from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        dq = deque([root])
        ret = []
        
        while len(dq):
            qlen, rsum = len(dq), 0
            
            for i in range(qlen):
                curr = dq.popleft()
                rsum += curr.val
                
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            
            ret.append(rsum / qlen)
        return ret
