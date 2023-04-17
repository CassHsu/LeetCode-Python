class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join(['[.]' if a == '.' else a for a in address])
