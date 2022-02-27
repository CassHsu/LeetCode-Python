class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birth = {}
        for log in logs:
            for alive in range(log[0], log[1]):
                if alive in birth:
                    birth[alive] += 1
                else:
                    birth[alive] = 1
                    
        return max(birth.items(), key = lambda x: (x[1],-x[0]))[0]
