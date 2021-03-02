class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        stones.sort()
        m1 = stones.pop()
        m2 = stones.pop()
        stones.append(m1 - m2)
        return self.lastStoneWeight(stones)
