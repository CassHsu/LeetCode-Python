class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center = 1
        num = len(edges)
        for i in range(1, num + 2):
            cnt = 0
            for e in edges:
                if i not in e:
                    break
                cnt += 1
            
            if cnt == num:
                center = i
                break
                    
        return center
