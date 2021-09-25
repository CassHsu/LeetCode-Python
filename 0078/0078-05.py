class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bfs(arr):
            if len(arr) == 0:
                return [[]]
            
            prev = bfs(arr[:-1])
            curr = [[*r, arr[-1]] for r in prev]
            return [*prev, *curr]
               
        return bfs(nums)
