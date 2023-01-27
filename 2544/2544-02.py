class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        signed = []

        def sign(i, s):
            if i < 0 or i >= len(digits):
                return

            if s < 0:
                signed.append(digits[i] * -1)
            else:
                signed.append(digits[i])
            
            sign(i + 1, s * -1)
                

        sign(0, 1)
        return sum(signed)
