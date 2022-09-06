class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result
        
        dq = collections.deque([root])
        
        while dq:
            count = len(dq)
            print('len: ', count)
            
            lvl = []
            while count:
                node = dq.popleft()
                lvl.append(node.val)
                
                for c in node.children:
                    dq.append(c)
                    
                count -= 1
                
            result.append(lvl)
        
        return result
