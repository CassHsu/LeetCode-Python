class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]
        
        total = sum(target)
        
        target = [-t for t in target]
        heapq.heapify(target)
        
        while -target[0] > 1:
            largest = -target[0]
            rest = total - largest
            
            if rest == 1:
                return True
            
            x = largest % rest
            
            if x == 0 or x == largest:
                return False
            
            heapq.heapreplace(target, -x)
            total = total - largest + x
            
        return True
