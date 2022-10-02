class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        peoples = []
        
        for i in range(n):
            peoples.append((names[i], heights[i]))
        
        peoples.sort(key=lambda p: p[1], reverse=True)
        
        return [p[0] for p in peoples]
