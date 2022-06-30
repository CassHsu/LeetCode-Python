class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda p: (-p[0], p[1]))
        
        for p in people:
            ans.insert(p[1], p)
        
        return ans
