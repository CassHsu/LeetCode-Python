class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        pairs = []
        size = len(hours)
        
        for i, h in enumerate(hours):
            for j in range(i + 1, size):
                if (hours[j] + h) % 24 == 0:
                    pairs.append((i, j))
                    
        return len(pairs)
