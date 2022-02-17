from collections import deque

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evens = sorted([nums[i] for i in range(0, n, 2)])
        odds = sorted([nums[i] for i in range(1, n, 2)], reverse=True)

        ans = []

        odds = deque(odds)
        evens = deque(evens)
        
        while len(odds) > 0 and len(evens) > 0:
            ans.append(evens.popleft())
            ans.append(odds.popleft())
        
        if len(evens) > 0:
            ans.append(evens.popleft())
        if len(odds) > 0:
            ans.append(odds.popleft())
        
        return ans
