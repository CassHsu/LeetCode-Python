class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''

        for a in address:
            ans += '[.]' if a == '.' else a

        return ans
