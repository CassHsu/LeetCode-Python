class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        signed = []

        def sign(i, s) -> bool:
            if i < 0 or i >= len(digits):
                return False
            if s < 0:
                signed.append(digits[i] * -1)
            else:
                signed.append(digits[i])
            return True

        def sign_r(i, s):
            if sign(i, s):
                sign_r(i + 1, s * -1)

        sign_r(0, 1)
        return sum(signed)
