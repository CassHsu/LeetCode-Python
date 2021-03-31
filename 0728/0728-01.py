class Solution:
    def check(self, num):
        x = num
        while x > 0:
            x, d = divmod(x, 10)
            if d == 0 or num % d > 0:
                return False
        return True
         
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right+1):
            if self.check(i):
                ret.append(i)
        return ret
