class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        qo = deque([original, ])
        qc = deque([cloned, ])
        
        while qo:
            no = qo.popleft()
            nc = qc.popleft()
            
            if no is target:
                return nc
            
            if no:
                qo.append(no.left)
                qo.append(no.right)
                
                qc.append(nc.left)
                qc.append(nc.right)
