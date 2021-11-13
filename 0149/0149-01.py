class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        count = {}
        
        for p1, p2 in combinations(map(tuple, points), 2):
            m = float("inf") if p1[0] == p2[0] else (p1[1] - p2[1]) / (p1[0] - p2[0])
            
            b = p1[0] if p1[0] == p2[0] else p1[1]- m * p1[0]
            if (m, b) in count:
                count[(m, b)] |= set([p1, p2])
            else:
                count[(m, b)] = set([p1, p2])

        return max([1] + [len(count[x]) for x in count])
