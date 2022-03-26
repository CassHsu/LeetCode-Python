class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda l : l[0] - l[1])
        
        countA, total = 0, 0
        half = len(costs) // 2
        for a, b in costs:
            if countA < half:
                total += a
                countA += 1
            else:
                total += b
        return total
