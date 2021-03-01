class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        
        while True:
            stones.sort(reverse=True)
            y = stones[0]
            x = stones[1]
            stones[0] = stones[1] = 0;
            
            if x == 0:
                return y
            
            if x != y:
                stones[0] = y - x;
        return 0
