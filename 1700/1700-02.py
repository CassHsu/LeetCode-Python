from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if students.count(1) == sandwiches.count(1):
            return 0
        
        qSandwiches = deque(sandwiches)
        qStudents = deque(students)
        
        n = len(students)
        round = (n - 1) * (n - 1)
        
        last = ''.join(str(s) for s in qStudents)
        while round > 0:
            student = qStudents.popleft()
            if student != qSandwiches[0]:
                qStudents.append(student)
            else:
                qSandwiches.popleft()
            
            if len(qSandwiches) == 0:
                break
                
            now = ''.join(str(s) for s in qStudents)
            if now == last:
                break
            
            last = now
            round -= 1

        return len(qStudents)