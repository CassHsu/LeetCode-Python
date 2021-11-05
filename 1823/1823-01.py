class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dq = collections.deque([i for i in range(1, n + 1)])
        
        while len(dq) != 1:
            dq.rotate(-k)
            dq.pop()
        
        return dq.pop()
