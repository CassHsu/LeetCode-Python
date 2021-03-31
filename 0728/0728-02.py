class Solution:
    def check(self, num):
        for n in str(num):
            if n == "0" or (num % int(n)) != 0:
                return False
        return True
         
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right+1):
            if self.check(i):
                ret.append(i)
        return ret
