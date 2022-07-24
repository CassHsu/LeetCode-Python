from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        res, sorted_list = deque(), SortedList()
        
        for n in nums[::-1]:
            res.appendleft(sorted_list.bisect_left(n))
            sorted_list.add(n)
            
        return res
