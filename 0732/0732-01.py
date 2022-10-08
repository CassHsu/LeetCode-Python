from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()
        

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        curr = res = 0
        
        for delta in self.diff.values():
            curr += delta
            res = max(curr, res)
            
        return res
