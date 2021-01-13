from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if students.count(1) == sandwiches.count(1):
            return 0
        
        qSandwiches = deque(sandwiches)
        qStudents = deque(students)
        
        while len(qSandwiches) > 0:
            if qSandwiches[0] not in qStudents:
                break
            
            s = qStudents.popleft()
            if qSandwiches[0] == s:
                qSandwiches.popleft()
            else:
                qStudents.append(s)
                
        return len(qStudents)