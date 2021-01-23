class Solution:
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n+1):
            im3 = i % 3
            im5 = i % 5
            if im3 == 0 and im5 == 0:
                res.append("FizzBuzz")
            elif im3 == 0:
                res.append("Fizz")
            elif im5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res