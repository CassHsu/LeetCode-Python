class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = bal = 0

        for i, c in enumerate(s):
            if c == '(':
                bal += 1
            else:
                bal -= 1

                if s[i - 1] == '(':
                    ans += 1 << bal

        return ans
