class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:
            return 0
        
        count_h = 0
        curr_h = int(current[:2])
        target_h = int(correct[:2])
        while curr_h < target_h:
            curr_h += 1
            count_h += 1
            
        count_m = 0
        curr_m = int(current[3:])
        target_m = int(correct[3:])
        
        if target_m == curr_m:
            return count_h
            
        if target_m < curr_m:
            count_h -= 1
            target_m += 60
        
        while curr_m < target_m:
            t = target_m - curr_m
            if t >= 15:
                curr_m += 15
            elif t >= 5:
                curr_m += 5
            else:
                curr_m += 1
                
            count_m += 1
                
        return count_h + count_m
