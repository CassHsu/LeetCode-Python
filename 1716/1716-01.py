class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = int(n / 7)
        remainder = int(n % 7)
        
        total = 0
        monday = 1
        
        for w in range(weeks):
            tmp = monday
            for i in range(7):
                total += tmp
                tmp += 1
            monday += 1
        
        tmp = monday
        for r in range(remainder):
            total += tmp
            tmp += 1
        
        return total